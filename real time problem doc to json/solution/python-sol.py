from striprtf.striprtf import rtf_to_text 
import json

head=[]
data=[]
out=[]

   
def Init():
        
    with open("Input/Sample.rtf", 'r') as file: 
        rtf_text = file.read() 
    plain_text = rtf_to_text(rtf_text) 
    split_line=plain_text.split("\n")
    headers=split_line[3:4]
    headers=headers[0].split("|")
    raw_data=split_line[4:-2]
    
    temp=[]    
    for line in raw_data:
        if line != "|":
            temp.append(line)
    global head
    head=headers[:-1]
    global data
    data=temp   

def Create():
    details={}
    cheack_key=0
    global out
    temp=[]

    for key in data:
        values=key.split("|")
        if str(cheack_key+1)==values[0][3:]:
            validate_key=True
        else:
            validate_key=False

        for value in range(len(values)-1):
            details[head[value]]=values[value]

        if validate_key:
            if temp != []:
                sub_row=out[-1]
                sub_row["MarkDetails"]=temp
                out.pop()
                out.append(sub_row)
            out.append(details)
            details={}
            cheack_key=cheack_key+1
            temp=[]
        else:
            temp.append(details)
            details={}
def Final_result():
    temp_json={
                    "Interview": "Interview",
                    "Test": "ABC-301",
                    "Reportname": "Question",
                    "ReturnMessage": "Successful",
                    "MarkDetails": []
                }
    temp_json["MarkDetails"]=out
    temp_json=[temp_json]
    final_json=json.dumps(temp_json)
    print(final_json)              
            
Init()
Create()
Final_result()
    

