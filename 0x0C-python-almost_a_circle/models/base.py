#!/usr/bin/python3

"""this is the module contain Bse class"""

import json
import csv
import turtle
import os


class Base:
    """doc for this calss"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the class constractor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list")
        if any(type(i) != dict for i in list_dictionaries):
            raise TypeError("list_dictionaries must contain dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to the file"""
        if type(list_objs) != list and list_objs is not None:
            raise TypeError("list_objs must be a list")
        if list_objs == [] or list_objs is None:
            wr = []
        else:
            ty = type(list_objs[0])
            if any(type(i) != ty for i in list_objs):
                raise ValueError("all elements of list_objs must match")
            wr = [i.to_dictionary() for i in list_objs]
        fname = cls.__name__+".json"
        with open(fname, "w") as f:
            content = cls.to_json_string(wr)
            f.write(content)

    @staticmethod
    def from_json_string(json_string):
        """to the string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """second class method"""
        dummy = cls(2, 3) if cls.__name__ == "Rectangle" else cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load"""
        the_load = ""
        ret = []
        try:
            with open(cls.__name__+".json") as f:
                the_load = f.read()
        except Exception as e:
            return []
        ins = cls.from_json_string(the_load)
        ret = [cls.create(**x) for x in ins]
        return ret

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save csv"""
        fname = cls.__name__+".csv"
        sfields = ['id', 'size', 'x', 'y']
        rfields = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == "Rectangle":
            header = rfields
        else:
            header = sfields

        with open(fname, "w") as f:
            if list_objs is not None:
                data = [i.to_dictionary() for i in list_objs]
                fi = csv.writer(f, fildnames=header)
                fi.writerow(list_objs)
                writer.writeheader()

    @classmethod
    def load_from_file_csv(cls):
        """lode from csv"""
        fname = cls.__name__+".csv"
        sfields = ['id', 'size', 'x', 'y']
        rfields = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == "Rectangle":
            header = rfields
        else:
            header = sfields
        ret = []
        if os.path.exists(fname):
            with open(filename) as f:
                result = csv.reader(f, delimiter=", ")
                for index, val in enumerate(result):
                    if i > 0:
                        dummy = cls(1, 1)
                        for x, y in enumerate(val):
                            if y:
                                setattr(dummy, header[x], int(y))
                        ret.append(dummy)
        return ret

    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module"""
        turt = turtle.Turtle()
        turt.shape("turtle")
        turt.pensize(4)
        turt.screen.bgcolor("black")

        turt.color("#123456")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)

        turt.color("Green")
        for sq in list_squares:
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(4):
                turt.forward(sq.width)
                turt.left(90)
        turt.hideturtle()
        turtle.exitonclick()
