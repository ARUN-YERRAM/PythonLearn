# # lists=["Kiwi","Kiya","rover","knight"]
# # # newlist=[x if x=="rover"  else "kiwi" for x in list] 
# # # newlist=[x.upper() for x in list]
# # # print(newlist)   \
# # # list.sort(key=str.lower)
# # # list.reverse()
# # # print(list)
# # # list1=list.copy()
# # list2=[1,2,3.445,"snn"]
# # # list3=lists+list2
# # # list1=list(lists)
# # # print(list3)
# # for x in lists:
# #     list2.append(x)
# # print(list2)    

# #include<Stepper.h>
# int stepsPerRevolution=400;
# Stepper myStepper(stepsPerRevolution,2,3,4,5);
# void setup() {
# myStepper.setSpeed(60);
# Serial.begin(9600);
# }
# void loop() {
# Serial.println("clockwise");
# myStepper.step(stepsPerRevolution);
# delay(15);
# Serial.println("counterclockwise"); 
# myStepper.step(-stepsPerRevolution);
# delay(20);
# }
