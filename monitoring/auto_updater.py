import subprocess
import schedule
import time
from github import Github

def update_project():
    # Actualizar código desde GitHub
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo("tu_usuario/tiktok-bot")
    if repo.get_commits()[0].sha != open('last_commit.txt').read():
        subprocess.run(["git", "pull", "origin", "main"])
        subprocess.run(["pip", "install", "-r", "requirements.txt", "--upgrade"])
        open('last_commit.txt', 'w').write(repo.get_commits()[0].sha)

# Programar actualizaciones cada 24 horas
schedule.every(24).hours.do(update_project)

while True:
    schedule.run_pending()
    time.sleep(60)