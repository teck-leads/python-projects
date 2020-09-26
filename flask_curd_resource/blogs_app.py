from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)
                 
                 
blogs = {}

class BlogsAPI(Resource):
    def get(self, blog_id=None):
        if blog_id is None:
            return blogs
        if blog_id not in blogs:
            abort(404, message="blog_id {} doesn't exist".format(blog_id))
        print(blogs[blog_id])
        return blogs[blog_id]
        # '''Return 'blogs' dictionary if 'blog_id' is None.
        
        #    if blog_id is provided,
        #    Abort the request if 'blog_id' and not in keys of 'blogs' dictionary, or else
        #    Return the blog corresponding to given 'blog_id'
        # '''

    
    def post(self, blog_id):
        
        if blog_id not in blogs:
            # data=request.get_json()
            # blog={'title': data['title'], 'article_text':data['article_text']}
            blog={'title': request.form['title'], 'article_text':request.form['article_text']}
            blogs[blog_id] = blog

            return blog
        abort(404, message="blog_id {} already exists".format(blog_id))
        # '''
        # If 'blog_id' is not in keys of 'blogs' dictionary, create a new dictionary object
        # 'blog', with three keys 'title', 'article_text', and 'created_at'.
        # The values of 'title', and 'article_text' to be captured from http form varaibles :
        # 'title', 'article_text.
        # The value of 'created_at' must be current date time string represented by format '%Y-%m-%d %H:%M:%S'
        
        # Add the created dictionary object to 'blogs' dictionary with key corresponding to given 'blog_id',
        # and Return the created dictionary object.
        
        # If 'blog_id' is in keys of 'blogs' dictionary, abort the request.
        # '''
        
    
    def put(self, blog_id):
        if blog_id not in blogs:
            abort(404, message="Blog_Id "+str(blog_id)+" doesn't exist")
        
        blog={'title': request.form['title'],'article_text':blogs[blog_id]['article_text']}
        blogs[blog_id] = blog
        return blog
        # '''
        # If given 'blog_id' not in 'blogs' dictionary abort the request with 404 status code and message like shown below.
        
        # Sample Error message : "Blog_Id 2 doesn't exist"
        
        # Else, update the details of blog, identified by given 'blog_id', and return the updated blog details.
        # '''
        
    
    def delete(self, blog_id):
        if blog_id in blogs:
            response_string = 'Blog with Id '+str(blog_id)+' is deleted'
            del blogs[blog_id]
            return response_string
            
        abort(404, message="Blog_Id "+str(blog_id)+" doesn't exist")

        # '''
        # If 'blog_id' not in keys of 'blogs' dictionary, abort the request with 404 status code and message like shown below.
        
        # Sample Error message : "Blog_Id 2 doesn't exist"
        
        # Else delete the blog corresponding to given 'blog_id' from 'blogs' dictionary and respond with a message like shown below.
        
        # Sample Delete response message : "Blog with Id 3 is deleted"
        # '''
        
    
api.add_resource(BlogsAPI, '/blogs/',
                              '/blogs/<int:blog_id>/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)