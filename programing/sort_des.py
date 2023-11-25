N=int(input("Enter lenth of list:"))
app=[]
for i in range(N):
    app.append(int(input()))

for x in range(len(app)-1):
    for y in range(x+1,len(app)):
        if app[x] < app[y]:
            temp=app[x]
            app[x]=app[y]
            app[y]=temp
print(app)
