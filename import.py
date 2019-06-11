import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://xcwsszopsfqsvs:f40faf822248f604ed3bb9c9b4444cbf1a9e28c606afd9ee8eacc0801c95688f@ec2-54-227-245-146.compute-1.amazonaws.com:5432/d4hv2ctgd22sgh
')
db = scoped_session(sessionmaker(bind=engine))
def main():
    f = open("books.csv", "r") 
    reader = csv.reader(f)
    next(reader)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
               {"isbn": isbn, "title": title, "author": author, "year": year})
        db.commit()
        print(f"Added book with ISBN: {isbn} Title: {title}  Author: {author}  Year: {year}")
if __name__ == '__main__':
    main()
