from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, CHAR, VARCHAR, Integer, String, Text, DateTime, Float, Boolean, PickleType

Base = declarative_base()
db_uri = 'postgresql://webadmin:VCNtps41396@node37019-thanet.proen.app.ruk-com.cloud:11235/homework'
engine = create_engine(db_uri, echo=False)

class Students(Base):
    __tablename__ = 'Students' 
    student_id = Column(String(13),primary_key = True,nullable = True) 
    f_name = Column(String(30),nullable = False) 
    l_name = Column(String(30),nullable=False) 
    e_mail = Column(String(50), nullable=False) 

    def __repr__(self):
        return '<User(student_id = {}, f_name = {}, l_name = {}, e_mail ={})>'.format(self.student_id, self.f_name, self.l_name, self.e_mail)
        

class Registration(Base):
    __tablename__ = 'Registration' 
    id = Column(Integer(), primary_key = True)
    student_id = Column(String(13)) 
    subject_id = Column(String(15),nullable = False) 
    year = Column(String(4),nullable=False) 
    semester = Column(String(1),nullable=False)  
    grade = Column(String(2))

    def __repr__(self):
        return '<User(student_id = {}, subject_id = {}, year = {}, semester ={}, grade={})>'.format(self.student_id, \
            self.subject_id, self.year , self.semester, self.grade)

class Subjects(Base):
    __tablename__ = 'Subjects' 
    subject_id = Column(String(15),primary_key = True) 
    subject_name = Column(String(50),nullable = False) 
    credit = Column(Integer(),nullable=False) 
    teacher_id = Column(String(3),nullable=False) 
    def __repr__(self):
        return '<User(subject_id = {}, subject_name = {}, credit = {}, teacher_id ={})>'.format(self.subject_id, \
            self.subject_name, self.credit , self.teacher_id)

class Teacher(Base):
    __tablename__ = 'Teachers' 
    teacher_id = Column(String(3),primary_key=True, nullable=True)
    f_name = Column(String(50), nullable=True)
    l_name = Column(String(30), nullable=True)
    e_mail = Column(String(50), nullable=True)

    def __repr__(self):
            return '<User(teacher_id = {} , f_name= {} , l_name = {} , e_mail = {})>'.format(self.teacher_id,\
                    self.f_name, self.l_name , self.e_mail)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

user1 = Students(
    student_id ='6406022620029',
    f_name='Thanet',
    l_name='Suwannapirom',
    e_mail ='s6406022620029@email.kmutnb.ac.th'
)

user2 = Students(
    student_id ='6406022610015',
    f_name='Kongphop',
    l_name='Sri-On',
    e_mail ='s6406022610015@email.kmutnb.ac.th'
)

user3 = Students(
    student_id ='6406022620053',
    f_name='Watcharakorn',
    l_name='Yentaweesub',
    e_mail ='s6406022620053@email.kmutnb.ac.th'
)

re1 = Registration(
    student_id ='6406022620029',
    subject_id='060233113',
    year='2565',
    semester ='1',
    grade = 'A'
)

re1_2 = Registration(
    student_id ='6406022620029',
    subject_id='060233201',
    year='2565',
    semester ='1',
    grade = 'A'
)

re1_3 = Registration(
    student_id ='6406022620029',
    subject_id='060233205',
    year='2565',
    semester ='1',
    grade = 'A'
)


re2 = Registration(
    student_id ='6406022610015',
    subject_id='060233113',
    year='2565',
    semester ='1',
    grade = 'A'
)

re2_2 = Registration(
    student_id ='6406022610015',
    subject_id='060233201',
    year='2565',
    semester ='1',
    grade = 'B+'
)

re2_3 = Registration(
    student_id ='6406022610015',
    subject_id='060233205',
    year='2565',
    semester ='1',
    grade = 'A'
)

re3 = Registration(
    student_id ='6406022620053',
    subject_id='060233113',
    year='2565',
    semester ='1',
    grade = 'A'
)

re3_2 = Registration(
    student_id ='6406022620053',
    subject_id='060233201',
    year='2565',
    semester ='1',
    grade = 'B+'
)

re3_3 = Registration(
    student_id ='6406022620053',
    subject_id='060233205',
    year='2565',
    semester ='1',
    grade = 'B'
)

sub1 = Subjects(subject_id ='060233113',subject_name='ADVANCED COMPUTER PROGRAMMIN',credit='3',teacher_id ='AMK')
sub2 = Subjects(subject_id ='060233201',subject_name='NETWORK ENGINEERING LABORATO',credit='1',teacher_id ='WKN')
sub3 = Subjects(subject_id ='060233205',subject_name='ADVANCED NETWORK AND PROTOCOL',credit='3',teacher_id ='KNM')

T1 = Teacher(teacher_id='AMK',f_name='Anirach',l_name='Mingkhwan',e_mail='Anirach@gmail.com')
T2 = Teacher(teacher_id='WKN',f_name='Watcharachai',l_name='Kongsiriwattana',e_mail='Watcharachai@gmail.com')
T3 = Teacher(teacher_id='KNM',f_name='Khanista',l_name='Namee',e_mail='Khanista@gmail.com')

session.add_all([user1,user2,user3,re1, re1_2,re1_3, re2, re2_2,re2_3, re3,re3_2, re3_3,sub1 ,sub2,sub3,T1,T2,T3])
session.commit()