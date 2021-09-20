from flask import session, redirect
from functools import wraps

# define function login_requirements that receives another function as an argument
def login_required(func):
  @wraps(func)
  def wrapped_function(*args, **kwargs):
    # if logged in, call original function with original arguments
    if session.get('loggedIn') == True:
      return func(*args, **kwargs)

    return redirect('/login')
  
  return wrapped_function