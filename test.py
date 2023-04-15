from app.models import Post

posts = Post.query.all()
for post in posts:
  print(post.title, post.vote_count)
