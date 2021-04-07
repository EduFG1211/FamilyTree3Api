from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

db = SQLAlchemy()

class Parent(db.Model):
    __tablename__ = 'parent'
    id = db.Column(db.Integer, primary_key=True)
    son_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    father_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=True)
    mother_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=True) 

    def serialize(self):
        return {
            "id": self.id,
            "father_id": self.father_id,
            "mother_id": self.mother_id,
            "son_id": self.son_id,
        }

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    # father = db.relationship(Parent)
    # mother = db.relationship(Parent)

    def getAllPerson():
        list_person = Person.query.all()
        list_person = list(map(lambda x: x.serialize(), list_person))
        list_person.sort(key=lambda x: x["age"], reverse=True) 
        return(list_person)

    def getSpecificMember(id):
        member = Person.query.filter_by(id=id).first()
        person = {
            "name": member.name,
            "last_name": member.last_name,
            "age": member.age,
        }
        return person

    def getAllParent(son_id):
        member = Parent.query.filter_by(son_id=son_id).first()
        if member is None:
            return "No tiene padres"
        father = Person.getSpecificMember(member.father_id)
        mother = Person.getSpecificMember(member.mother_id)
        response = {
            "father": father,
            "mother": mother
        }
        return response

    def getAllSons(id):
        member_list = Parent.query.filter(or_(Parent.father_id==id, Parent.mother_id==id))
        if member_list is None:
            return "No tiene hijos"
        member_list = list(map(lambda x: Person.getSpecificMember(x.son_id), member_list))
        if len(member_list) == 0:
            return "No tiene hijos"
        response = {
            "sons": member_list
        }
        return response

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
        }