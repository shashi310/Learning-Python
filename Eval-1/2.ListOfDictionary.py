
def max_sallery_emp(emp):
    max=0
    for i in emp:
        if(i.sallery>=max):
            max=i.sallery
    print(max)

    for i in emp:
        if(i.sallery==max):
          return i


emp=[{
    "name": "Shashi",
    "sallery":2000,
    "designation":"intern",
},
{
    "name": "sk",
    "sallery":3000,
    "designation":"jr-dev",
},
{
    "name": "ka",
    "sallery":5000,
    "designation":"sr-dev",
}
]

ans=max_sallery_emp(emp)
print(ans)