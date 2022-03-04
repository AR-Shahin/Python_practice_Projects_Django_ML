

class A():
    @classmethod
    def sayHi(self, name):
        print("Hello {}".format(name))

    def __str__(self):
        return "Ssss"
# A.sayHi("Shahin")


st = """
The bar chat gives information about the number of men and women studying university at Australian universities. It shows that the number of student was male and the number of student was female. In this bar chart, we can see that, the every year the majority of male students are studying engineering.In 1992, the number of men students is 14000 and the number of women students is only 2000. That is too much minority from the men students. After ten years in 2002, the number of men students is 12000 and the number of women students is 4000. We can see that after ten years the number of women students has been increased slightly and the number of men students has been decreased. Well, after ten years in 2012, the number of male students is the same as the previous survey and the number of women students has been increased from the previous survey.Overall, we can say that the number of women students has been increasing gradually in Australian universities.
"""


print(len(st.split(" ")))
