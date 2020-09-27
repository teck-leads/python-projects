from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with, marshal
import datetime as dt

app = Flask(__name__)
api = Api(app)
               
blogsParser = reqparse.RequestParser()
blogsParser.add_argument('title', required=True, type=str)
blogsParser.add_argument('article_text', required=True, type=str)

# Create a dictionary named 'blog_fields' with
# three fields 'title', 'article_text' and
# 'created_at' as string type.
blog_fields = {
    'title': fields.String,
    'article_text': fields.String,
    'created_at': fields.String
}

blogs = {}

class BlogsAPI(Resource):
    @marshal_with(blog_fields)
    def get(self, blog_id=None):

        if blog_id is None:
            return [ blogs[blog_id] for blog_id in blogs ]
        if blog_id not in blogs:
            abort(404, message="Blog_Id {} doesn't exist".format(blog_id))
        return blogs[blog_id]
    
    @marshal_with(blog_fields)
    def post(self, blog_id):

        blog_args = blogsParser.parse_args()
        if blog_id not in blogs:
            blog = {}
            
            blog['title'] = blog_args['title']
            blog['article_text'] = blog_args['article_text']
            created_at = dt.datetime.now()
            blog['created_at'] = created_at.strftime('%Y-%m-%d %H:%M:%S')
            blogs[blog_id] = blog
            return blog
        abort(404, message="Blog_Id {} already exists".format(blog_id))
    
    @marshal_with(blog_fields)
    def put(self, blog_id):

        blog_args = blogsParser.parse_args()
        if blog_id in blogs:
            blog = {}
            
            blog['title'] = blog_args['title']
            blog['article_text'] = blog_args['article_text']
            
            blogs[blog_id].update(blog)
            return blogs[blog_id]
        abort(404, message="Blog_Id {} doesn't exist".format(blog_id))
    
    def delete(self, blog_id):

        if blog_id in blogs:
            response_string = 'Blog with Id {} is deleted'.format(blog_id)
            del blogs[blog_id]
            return response_string
        abort(404, message="Blog_Id {} doesn't exist".format(blog_id))
    
api.add_resource(BlogsAPI, '/blogs/',
                              '/blogs/<int:blog_id>/')

if __name__ == '__main__':
    app.run()