from scraping import scraping
import time

def main():
    while True:
        scraping()
        time.sleep(3600) # attendi 1 ora (3600 secondi)



# chiamata della funzione "main" quando viene eseguito il programma
if __name__ == "__main__":
    main()