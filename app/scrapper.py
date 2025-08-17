from app.api.fetch import fetch
from app.sections.post_section import PostSection
from app.api.mail import send_email
from app.utils.post_helper import post_already_sent, save_post

def run_post_scrapper():    
    keywords = ("post-utml", "admission", "screening", "exam", "exams")
    page_content = fetch()
    page = PostSection(page_content)
    posts = page.posts

    for post in posts:
        if any(k in (post.title + post.description).lower() for k in keywords):
            if not post_already_sent(post.url):
                mail_content = (
                    f"Title: {post.title.upper()} - URL: {post.url}\n"
                    f"Description: {post.description}"
                    f"Thumbnail: https://uniben.edu/{post.thumbnail}\n"
                )

                save_post(title=post.title, description=post.description, url=post.url, thumbnail=post.thumbnail)
                print('Sending Mail....', mail_content)
                send_email(mail_content)
            else:
                print(f"✅ Skipping already sent post: {post.url}")

            
