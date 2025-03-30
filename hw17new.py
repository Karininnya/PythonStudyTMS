from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/elibrary_orm_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), unique=True, nullable=False)
    authors = relationship("BookAuthor", back_populates="book", cascade="all, delete")
    genres = relationship("BookGenre", back_populates="book", cascade="all, delete")


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), unique=True, nullable=False)
    books = relationship("BookAuthor", back_populates="author", cascade="all, delete")


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    books = relationship("BookGenre", back_populates="genre", cascade="all, delete")


class BookAuthor(Base):
    __tablename__ = "books_authors"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"))
    book = relationship("Book", back_populates="authors")
    author = relationship("Author", back_populates="books")


class BookGenre(Base):
    __tablename__ = "books_genres"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))
    genre_id = Column(Integer, ForeignKey("genres.id", ondelete="CASCADE"))
    book = relationship("Book", back_populates="genres")
    genre = relationship("Genre", back_populates="books")


def init_db():
    Base.metadata.create_all(engine)


def get_all_books():
    with SessionLocal() as session:
        return session.query(Book).all()


def get_all_authors():
    with SessionLocal() as session:
        return session.query(Author).all()


def get_all_genres():
    with SessionLocal() as session:
        return session.query(Genre).all()


def get_book_full_info_by_id(book_id):
    with SessionLocal() as session:
        book = session.query(Book).filter(Book.id == book_id).first()
        if not book:
            return None
        return {
            "book_info": book,
            "authors": [ba.author.full_name for ba in book.authors],
            "genres": [bg.genre.name for bg in book.genres],
        }


def create_author(full_name):
    with SessionLocal() as session:
        author = Author(full_name=full_name)
        session.add(author)
        session.commit()


def search_book(query):
    with SessionLocal() as session:
        return session.query(Book).filter(Book.title.ilike(f"%{query}%")).all()