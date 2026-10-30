 
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        message = request.form.get("message", "")

        with open("contact_messages.txt", "a", encoding="utf-8") as file:
            file.write(f"Date: {datetime.now()}\n")
            file.write(f"Name: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Message: {message}\n")
            file.write("-" * 40 + "\n")

        return """
        <html>
        <head><title>Message Received</title></head>
        <body style="font-family:Arial;text-align:center;padding:60px;background:#f0f6ff">
            <h1 style="color:#0877cc">Thank you!</h1>
            <p>Your message has been saved successfully.</p>
            <a href="/">Return to Home</a>
        </body>
        </html>
        """

    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My ICT Portfolio</title>
        <style>
            * { box-sizing: border-box; }
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f7fc;
                color: #243247;
                line-height: 1.6;
            }
            header {
                background: #073b70;
                color: white;
                padding: 22px 8%;
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
            }
            header h2 { margin: 0; }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 10px;
            }
            .hero {
                background: linear-gradient(135deg, #0756a0, #1596d4);
                color: white;
                text-align: center;
                padding: 80px 20px;
            }
            .hero h1 { font-size: 42px; margin-bottom: 10px; }
            .hero p { font-size: 19px; }
            .button {
                display: inline-block;
                background: white;
                color: #0756a0;
                padding: 12px 22px;
                border-radius: 6px;
                text-decoration: none;
                font-weight: bold;
                margin-top: 12px;
            }
            section {
                max-width: 1000px;
                margin: auto;
                padding: 45px 22px;
            }
            h2 { color: #0756a0; }
            .cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
            }
            .card {
                background: white;
                padding: 22px;
                border-radius: 12px;
                box-shadow: 0 4px 15px #00000010;
            }
            form {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 4px 15px #00000010;
            }
            input, textarea {
                width: 100%;
                padding: 12px;
                margin: 8px 0 16px;
                border: 1px solid #cbd5e1;
                border-radius: 6px;
                font: inherit;
            }
            button {
                background: #0756a0;
                color: white;
                border: 0;
                padding: 13px 22px;
                border-radius: 6px;
                cursor: pointer;
                font-size: 16px;
            }
            footer {
                background: #073b70;
                color: white;
                text-align: center;
                padding: 20px;
            }
        </style>
    </head>
    <body>
        <header>
            <h2>My ICT Portfolio</h2>
            <nav>
                <a href="#home">Home</a>
                <a href="#about">About</a>
                <a href="#projects">Projects</a>
                <a href="#contact">Contact</a>
            </nav>
        </header>

        <div class="hero" id="home">
            <h1>Welcome to My Portfolio</h1>
            <p>ICT Student | Aspiring Web Developer | Technology Enthusiast</p>
            <a class="button" href="#projects">View My Projects</a>
        </div>

        <section id="about">
            <h2>About Me</h2>
            <p>
                I am an ICT student developing my skills in computer systems,
                networking, programming and website development. I enjoy learning
                new technologies and solving computer-related problems.
            </p>
        </section>

        <section id="projects">
            <h2>My Projects</h2>
            <div class="cards">
                <div class="card">
                    <h3>Website Development</h3>
                    <p>Learning to build websites using HTML, CSS and Python Flask.</p>
                </div>
                <div class="card">
                    <h3>Computer Troubleshooting</h3>
                    <p>Practising how to identify and solve common computer problems.</p>
                </div>
                <div class="card">
                    <h3>Networking</h3>
                    <p>Learning about network devices, topologies and Ethernet cables.</p>
                </div>
            </div>
        </section>

        <section id="contact">
            <h2>Contact Me</h2>
            <p>Use the form below to send a message.</p>
            <form action="/" method="POST">
                <label for="name">Your Name</label>
                <input id="name" name="name" type="text" required>

                <label for="email">Your Email</label>
                <input id="email" name="email" type="email" required>

                <label for="message">Your Message</label>
                <textarea id="message" name="message" rows="5" required></textarea>

                <button type="submit">Send Message</button>
            </form>
        </section>

        <footer>
            <p>My ICT Portfolio | Built with Python and Flask</p>
        </footer>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)

