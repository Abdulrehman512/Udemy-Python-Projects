import webbrowser as wb

def work_auto():
    Chrome_Path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    URLS = ("stackoverflow.com",
            "google.com",
            "gmail.com",
            "github.com/Abdulrehman512",
            "youtube.com")
    for url in URLS:
        wb.get(Chrome_Path).open(url)
        
work_auto()