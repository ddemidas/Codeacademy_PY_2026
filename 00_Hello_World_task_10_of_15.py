quilt_side=6
quilt_fabric=(quilt_side**2)
print("For a quilt with side "+str(quilt_side) + "we need " + str(quilt_fabric)+" square meters of fabric")

quilt_side=7
quilt_fabric=(quilt_side**2)
print("For a quilt with side "+str(quilt_side) + "we need " + str(quilt_fabric)+" square meters of fabric")

quilt_side=8
quilt_fabric=(quilt_side**2)
print("For a quilt with side "+str(quilt_side) + "we need " + str(quilt_fabric)+" square meters of fabric")

quits_pro_person=6
persons_qty=6
fabric_total=quilt_fabric*quits_pro_person*persons_qty
print("In order to produce "+str(quits_pro_person)+ " pro person for " +str(persons_qty)+" persons we would need "+str(fabric_total)+" of fabric")