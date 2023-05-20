

# list=[[5,6,7],[7,8,9]]
# print(list[1][1])


print("Welcome to KBC")
sum=0
print()
questions=[
    ["Who made python?","Guido van Rossum","Elon Musk","Jeff Bezos","Binod Chaudhary","a"],
    ["Which language was used to made FaceBook?","Python","Java","Php","C++","c"],
    ["Where is the birthplace of Buddha?","Kapilvastu","Kathmandu","Lumbini","Delhi","c"],
    ["Which is the most popular language?","Python","Java","Php","C++","a"],
    ["What is the most popular AI?","Python","Siri","Alexa","ChatGpt","d"],
    ["Who has made 100 videos on python","Harry","Logan Paul","Moss Hamdani","Jenny","a"],
    ["Which is the most popular girl band group","Fifth Harmony","Black Pink","Fifty-Fifty","BTS","b"],
    ["Who is the owner of Facebook","Elon Musk","Nicola Tesla","Mark Zuckerburg","Ambani","c"],
    ["Which is the tallest mountain of the World","Mt.K2","Mt.Fuji","Mt. Kanchanjunga","Mt.Everest","d"]
 
]

levels=[10000,20000,30000,40000,100000,800000,2000000,3000000,4000000]
# for j in range(len(levels)):
#     sum=sum+levels[j]
# print(sum)

for i in range(len(questions)):
    print()
    #question=questions[i]
    print(f"{questions[i][0]}")
    print("Your options are: ")
    print(f"a.{questions[i][1]}           b.{questions[i][2]}")
    print(f"c.{questions[i][3]}           d.{questions[i][4]}")

    ans=input("Answer: ")
    if(ans==questions[i][5]):
        print("You are correct!")
        sum=sum+levels[i]
        print(f"You have won {sum}, Congratulations!")
    else:
        print("You have lost")
        print(f"You have won total of {sum}, Congratulations!")
        break

print()
if(sum==10000000):
    print("Congratulations in becoming a Crorepati!!")

print()
print("Thank you for coming!")  
