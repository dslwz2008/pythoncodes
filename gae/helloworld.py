#coding:utf-8
import webapp2
from cgi import escape
import jinja2
import os
import re
from google.appengine.ext import db
from google.appengine.api import memcache
from string import letters
from datetime import datetime, timedelta
import random
import hashlib
import hmac
import json 

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), 
    autoescape = True)

def render_str(template, **params):
    t = jinja_environment.get_template(template)
    return t.render(params)
    
class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
class MainPage(webapp2.RequestHandler):
    def get(self):
#        self.response.headers['Content-Type'] = 'text/html'#this is default
#        self.response.write(html_mainpage)
        greetings = ['hello', 'hi', 'how are you']
        template_values = {
            'greetings': greetings,
            'url': 'ytxwz.sinaapp.com'
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))
        
    def post(self):
#        user_month = valid_month(self.request.get('month'))
#        user_day = valid_day(self.request.get('day'))
#        user_year = valid_year(self.request.get('year'))
#
#        if not(user_month and user_day and user_year):
#            self.response.out.write(form)
#        else:
#            self.response.out.write("Thanks! That's a totally valid day!")
        pass
    
class TestFormHandler(webapp2.RequestHandler):
    def get(self):
        #q = self.request.get('q')
        #self.response.write(q)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)
        
    def post(self):
        q = self.request.get('q')
        self.response.write(q)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)
        
#Hello->Uryyb->Hello
#1.标点符号不变，空格
#2.escape html
class ROT13Handler(BaseHandler):        
    def rotchar(self, char):
        result=0
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            result = ord(char)+13 if ord(char)+13 <= ord('z') else ord(char)-13
        elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
            result = ord(char)+13 if ord(char)+13 <= ord('Z') else ord(char)-13
        return chr(result)
        
    def rot13(self, raw):
        rawlist = list(raw)
        result = []
        for item in rawlist:
            if item.isalpha():
                result.append(self.rotchar(item))
            else:
                result.append(item)
        return ''.join(result)
        
    def get(self):
        template = jinja_environment.get_template('rot13.html')
        self.response.out.write(template.render())
        
    def post(self):
        text = self.request.get('text')
        print text
        rotted = self.rot13(text)
        template = jinja_environment.get_template('rot13.html')
        self.response.out.write(template.render({'content':rotted}))
        
#
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r'^.{3,20}$')
EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

def valid_username(username):
    return USER_RE.match(username)
    
def valid_password(password):
    return PASSWORD_RE.match(password)
    
def valid_email(email):
    return EMAIL_RE.match(email)
    
class SignUpHandler(BaseHandler):
    def get(self):
        template = jinja_environment.get_template('signup.html')
        self.response.out.write(template.render({}))
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        temp_valus = {}
        error = False
        
        temp_valus['username'] = username
        if not valid_username(username):
            temp_valus['error_username'] = "That's not a valid username"
            error = True
        if not valid_password(password):
            temp_valus['error_password'] = "That wasn't a valid password"
            error = True
        if password != verify:
            temp_valus['error_verify'] = "Your password didn't match"
            error = True
        temp_valus['email'] = email
        if email and not valid_email(email):
            temp_valus['error_email'] = "That's not a valid email"
            error = True
        
        if error:
            template = jinja_environment.get_template('signup.html')
            self.response.out.write(template.render(temp_valus))
        else:
            #template = jinja_environment.get_template('welcome.html')
            #self.response.out.write(template.render({'username' : username}))
            self.redirect('/unit2/welcome?username='+username)

class WelcomeHandler(BaseHandler):
    def get(self):
        username = self.request.get('username')
        template = jinja_environment.get_template('welcome.html')
        self.response.out.write(template.render({'username' : username}))

#class BlogHandler(BaseHandler):
#    def get(self):
#        blogs = Blog.all().order('created')
#        template = jinja_environment.get_template('blog.html')
#        self.response.out.write(template.render({'blogs':blogs}))
        
class NewPostHandler(BaseHandler):
    def get(self):
        template = jinja_environment.get_template('newpost.html')
        self.response.out.write(template.render({}))
    def post(self):
        title = self.request.get('subject')
        content = self.request.get('content')
        if title and content:
            blog = Blog(title=title, body=content)
            key = blog.put()
            self.redirect("/unit3/blog/%d" % key.id())
        else:
            errors = 'you must have a subject and contents'
            template = jinja_environment.get_template('newpost.html')
            self.response.out.write(template.render({'subject':title, 
            'content':content, 'errors':errors}))

class Blog(db.Model):
    title = db.StringProperty(required = True)
    body = db.TextProperty(required = True)
    created = db.DateProperty(auto_now_add = True)
    
class Permalink(BaseHandler):
    def get(self, blog_id):
        blog = Blog.get_by_id(int(blog_id))
        template = jinja_environment.get_template('front.html')
        self.response.out.write(template.render({'blog':blog}))
        
###################unit 4######################
secret = 'abcd'
class BlogHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        params['user'] = self.user
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_json(self, d):
        json_txt = json.dumps(d)
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        self.write(json_txt)
        
    def set_secure_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))
        
        if self.request.url.endswith('.json'):
            self.format = 'json'
        else:
            self.format = 'html'
        
def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val
        
##### user stuff
def make_salt(length = 5):
    return ''.join(random.choice(letters) for x in xrange(length))

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)

def valid_pw(name, password, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)

def users_key(group = 'default'):
    return db.Key.from_path('users', group)
    
class User(db.Model):
    name = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid, parent = users_key())

    @classmethod
    def by_name(cls, name):
        u = User.all().filter('name =', name).get()
        return u

    @classmethod
    def register(cls, name, pw, email = None):
        pw_hash = make_pw_hash(name, pw)
        return User(parent = users_key(),
                    name = name,
                    pw_hash = pw_hash,
                    email = email)

    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u

class Signup(BlogHandler):
    def get(self):
        self.render("signup.html")

    def post(self):
        have_error = False
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')

        params = dict(username = self.username,
                      email = self.email)

        if not valid_username(self.username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(self.password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif self.password != self.verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if self.email and not valid_email(self.email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.render('signup.html', **params)
        else:
            self.done()

    def done(self, *a, **kw):
        raise NotImplementedError
        
class SignUpU4Handler(Signup):
    def done(self):
        #make sure the user doesn't already exist
        u = User.by_name(self.username)
        if u:
            msg = 'That user already exists.'
            self.render('signup.html', error_username = msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()
            self.login(u)
            self.redirect('/unit5/blog/welcome')
            
class WelcomU4Handler(BlogHandler):
    def get(self):
        if self.user:
            self.render('welcome.html', username = self.user.name)
        else:
            self.redirect('/unit5/blog/signup')
        
class LoginU4Handler(BlogHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/unit5/blog/welcome')
        else:
            msg = 'Invalid login'
            self.render('login.html', error = msg)
            
class LogoutU4Handler(BlogHandler):
    def get(self):
        self.logout()
        self.redirect('/unit5/blog/signup')

###unit5
def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)
    
class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)

    def as_dict(self):
        time_fmt = '%c'
        d = {'subject': self.subject,
             'content': self.content,
             'created': self.created.strftime(time_fmt),
             'last_modified': self.last_modified.strftime(time_fmt)}
        return d

class BlogFront(BlogHandler):
    def get(self):
        posts, age = get_posts()
        if self.format == 'html':
            self.render('frontu5.html', posts = posts, age = age_str(age))
        else: 
            return self.render_json([p.as_dict() for p in posts])

class PostPage(BlogHandler):
    def get(self, post_id):
        post_key = 'POST_' + post_id
        post, age = age_get(post_key)
        
        if not post:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            age_set(post_key, post)
            age = 0
            
        if not post:
            self.error(404)
            return
        if self.format == 'html':
            self.render("permalink.html", post = post, age = age_str(age))
        else:
            self.render_json(post.as_dict())

class NewPost(BlogHandler):
    def get(self):
        if self.user:
            self.render("newpostu5.html")
        else:
            self.redirect("/unit5/blog/login")

    def post(self):
        if not self.user:
            self.redirect('/unit5/blog')

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent = blog_key(), subject = subject, content = content)
            p.put()
            self.redirect('/unit5/blog/%s' % str(p.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpostu5.html", subject=subject, content=content, error=error)

class FlushHandler(BlogHandler):
    def get(self):
        memcache.flush_all()
        self.redirect('/unit5/blog')

def age_set(key, value):
    save_time = datetime.utcnow()
    memcache.set(key, (value, save_time))
    
def age_get(key):
    r = memcache.get(key)
    if r:
        value, save_time = r
        age = (datetime.utcnow() - save_time).total_seconds()
    else:
        value, age = None, 0
    return value, age
    
def add_post(ip, post):
    post.put()
    get_posts(update = True)
    return str(post.key().id())
    
def get_posts(update = False):
    q = Post.all().order('-created').fetch(limit = 10)
    mc_key = 'BLOGS'
    posts, age = age_get(mc_key)
    if update or posts is None:
        posts = list(q)
        age_set(mc_key, posts)
    return posts, age
    
def age_str(age):
    s= 'queried %s seconds ago'
    age = int(age)
    if age == 1:
        s = s.replace('seconds', 'second')
    return s % age

PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/unit2/testform', TestFormHandler), 
                               ('/unit2/rot13', ROT13Handler), 
                               ('/unit2/signup', SignUpHandler), 
                               ('/unit2/welcome', WelcomeHandler), 
                               ('/unit3/blog', BlogHandler), 
                               ('/unit3/blog/newpost', NewPostHandler), 
                               ('/unit3/blog/(\d+)', Permalink), 
                               ('/unit4/signup', SignUpU4Handler), 
                               ('/unit4/welcome', WelcomU4Handler), 
                               ('/unit4/login', LoginU4Handler), 
                               ('/unit4/logout', LogoutU4Handler), 
                               ('/unit5/blog?(?:.json)?', BlogFront),
                               ('/unit5/blog/([0-9]+)(?:.json)?', PostPage), 
                               ('/unit5/blog/newpost', NewPost),
                               ('/unit5/blog/signup', SignUpU4Handler), 
                               ('/unit5/blog/welcome', WelcomU4Handler), 
                               ('/unit5/blog/login', LoginU4Handler), 
                               ('/unit5/blog/logout', LogoutU4Handler), 
                               ('/unit5/blog/flush', FlushHandler), 
                               ('/final/signup', FinalSignup),
                               ('/final/login', FinalLogin),
                               ('/final/logout', FinalLogout),
                               ('/final/_edit' + PAGE_RE, FinalEditPage),
                               ('/final/_history' + PAGE_RE, FinalHistoryPage),
                               (PAGE_RE, WikiPage),
                               ],
                              debug=True)
