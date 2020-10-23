from java.io import FileInputStream

def target(serverTarget):
    targetsForDeployment = []
    targets = serverTarget.split('|')
    for target in targets: 
      if(target == '') :
        break;
      index=target.find(':')
      serverName=target[0:index]
      type=target[index+1:]
      nextName =str('com.bea:Name='+serverName+',Type='+type)
      targetsForDeployment.append(ObjectName(nextName))
    set('Targets',jarray.array(targetsForDeployment, ObjectName))
    #return targetsForDeployment


def createMaxWM(line):
  try:
    startEdit()
    cd('/')
    domainName = cmo.getName()
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,maxName,count,serverTarget) = items
     
    # Check if Maximum Threads Constraint name exist 
    cd('/SelfTuning/' + domainName)
    redirect('/dev/null','false')
    exist = ls('MaxThreadsConstraints/',returnMap='true')
    if maxName in exist:
      print('\n!!!! Maximum Threads Constraint: ' + maxName + ' already exist !!!!\n')
      exit(exitcode=1,defaultAnswer='y')
    print('\nCreate Max Thread Constrain: ' + maxName )
	
    # Create MaxThreadsConstraints 
    cmo.createMaxThreadsConstraint(maxName)
    
    # Target to server/cluster
    cd('/SelfTuning/' + domainName + '/MaxThreadsConstraints/' + str(maxName))
    target(serverTarget)
    #set('Targets',jarray.array(targetsForDeployment, ObjectName))
	
    # Set Up Count size
    cmo.setCount(int(count))

  except Exception, e:
    print e
	


def createMinWM(line):
  try:
    startEdit()
    cd('/')
    domainName = cmo.getName()
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,minName,count,serverTarget) = items
    
    # Check if Minimum Threads Constraint exist	
    cd('/SelfTuning/' + domainName)
    redirect('/dev/null','false')
    exist = ls('MinThreadsConstraints/',returnMap='true')
    if minName in exist:
      print('\n!!!! Minimum Threads Constraint: ' + minName + ' already exist !!!!\n')
      exit(exitcode=1,defaultAnswer='y')
    print('\nCreate Min Thread Constrain: ' + minName )
	
    # Create Minimum Threads Constraint
    cmo.createMinThreadsConstraint(minName)
	
    # Target to Server/Cluster
    cd('/SelfTuning/' + domainName + '/MinThreadsConstraints/' + str(minName))
    target(serverTarget)
    #set('Targets',jarray.array(targetsForDeployment, ObjectName))
	
    # Set up count Size
    cmo.setCount(int(count))

  except Exception, e:
    print e



def createCapacity(line):
  try:
    startEdit()
    cd('/')
    domainName = cmo.getName()
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,capName,count,serverTarget) = items
    
    # Check if Capacity Constraint exist 
    cd('/SelfTuning/' + domainName)
    redirect('/dev/null','false')
    exist = ls('Capacities/',returnMap='true')
    if capName in exist:
      print('\n!!!! Capacity Costraint : ' + capName + ' already exist !!!!\n')
      exit(exitcode=1,defaultAnswer='y')
    print('\nCreate Capacity Constraints : ' + capName )

    # Create Capacity Constraint
    cmo.createCapacity(capName)
  
    # Target to Server/Cluster
    cd('/SelfTuning/' + domainName + '/Capacities/' + str(capName))
    target(serverTarget)
  
    # Set up count Size
    cmo.setCount(int(count))

  except Exception, e:
    print e


def createResTimeReqClass(line):
  try:
    startEdit()
    cd('/')
    domainName = cmo.getName()
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,resName,goal,serverTarget) = items
    
    # Check if Capacity Constraint exist 
    cd('/SelfTuning/' + domainName)
    redirect('/dev/null','false')
    exist = ls('ResponseTimeRequestClasses/',returnMap='true')
    if resName in exist:
      print('\n!!!! Response Time Request Class : ' + resName + ' already exist !!!!\n')
      exit(exitcode=1,defaultAnswer='y')
    print('\nCreate Response Time Request Class : ' + resName )

    # Create Capacity Constraint
    cmo.createResponseTimeRequestClass(resName)
  
    # Target to Server/Cluster
    cd('/SelfTuning/' + domainName + '/ResponseTimeRequestClasses/' + str(resName))
    target(serverTarget)
  
    # Set up goal Size
    cmo.setGoalMs(int(goal))

  except Exception, e:
    print e



def createFairShareReqClass(line):
  try:
    startEdit()
    cd('/')
    domainName = cmo.getName()
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,fairName,fairShare,serverTarget) = items
    
    # Check if Capacity Constraint exist 
    cd('/SelfTuning/' + domainName)
    redirect('/dev/null','false')
    exist = ls('FairShareRequestClasses/',returnMap='true')
    if fairName in exist:
      print('\n!!!! Fair Share : ' + fairName + ' already exist !!!!\n')
      exit(exitcode=1,defaultAnswer='y')
    print('\nCreate Fair Share: ' + fairName )

    # Create Capacity Constraint
    cmo.createFairShareRequestClass(fairName)
  
    # Target to Server/Cluster
    cd('/SelfTuning/' + domainName + '/FairShareRequestClasses/' + str(fairName))
    target(serverTarget)
  
    # Set up goal Size
    cmo.setFairShare(int(fairShare))

  except Exception, e:
    print e



def createConReqClass(line):
  try:
    startEdit()
    cd('/')
    domainName = cmo.getName()
    items = line.split(',')
    items = [item.strip() for item in items]
    #(type,conReqName,partFairShare,serverTarget,context_user,context_group,context) = items
    (type,conReqName,serverTarget) = items
    
    # Check if Capacity Constraint exist 
    cd('/SelfTuning/' + domainName)
    redirect('/dev/null','false')
    exist = ls('ContextRequestClasses/',returnMap='true')
    if conReqName in exist:
      print('\n!!!! Context Request Classes : ' + conReqName + ' already exist !!!!\n')
      exit(exitcode=1,defaultAnswer='y')
    print('\nContext Request Classes : ' + conReqName )

    # Create Capacity Constraint
    cmo.createContextRequestClass(conReqName)
  
    # Target to Server/Cluster
    cd('/SelfTuning/' + domainName + '/ContextRequestClasses/' + str(conReqName))
    target(serverTarget)
  
    # Set up goal Size
    #cmo.setFairShare(int(fairShare))
    #cd('/SelfTuning/' + domainName + '/ContextRequestClasses/' + str(conReqName) + '/ContextCases/' + str(conReqName))
    #cmo.setUserName(context_user)
    #cmo.setGroupName(context_group)
    #cmo.setRequestClassName(context)

  except Exception, e:
    print e



def createWorkManager(line):
  try:
    startEdit()
    cd('/')
    domainName = cmo.getName()
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,wmName,maxWm,minWm,reqClass,Capacity,serverTarget) = items
     
    # Check if Work Manager already exist  
    cd('/SelfTuning/' + domainName)
    redirect('/dev/null','false')
    exist = ls('WorkManagers/',returnMap='true')
    if wmName in exist:
      print('\n!!!! Work Manager: ' + wmName + ' already exist !!!!\n')
      exit(exitcode=1,defaultAnswer='y')
  
    # Create Work Manager
    print('\nCreate Work Manager: ' + wmName )
    cmo.createWorkManager(wmName)

    # Assign maxWorkManager
    if maxWm == "None":
      cd('/SelfTuning/' + domainName + '/WorkManagers/' + str(wmName))
      cmo.setMaxThreadsConstraint(None)
    else:
      exist = ls('/SelfTuning/' + domainName + '/MaxThreadsConstraints/',returnMap='true')
      if maxWm in exist:
        cd('/SelfTuning/' + domainName + '/WorkManagers/' + str(wmName))
        cmo.setMaxThreadsConstraint(getMBean('/SelfTuning/' + domainName + '/MaxThreadsConstraints/' + str(maxWm)))
        print('- Assign Max Threads Constraint : ' + maxWm)
      else:
        print('- Max Threads Constraint ' + maxWm + ' Not found')

    # Assign minWorkManager
    if minWm == "None":
      cd('/SelfTuning/' + domainName + '/WorkManagers/' + str(wmName))
      cmo.setMinThreadsConstraint(None)
    else:
      exist1 = ls('/SelfTuning/' + domainName + '/MinThreadsConstraints/',returnMap='true')
      if minWm in exist1:
        cd('/SelfTuning/' + domainName + '/WorkManagers/' + str(wmName))
        cmo.setMinThreadsConstraint(getMBean('/SelfTuning/' + domainName + '/MinThreadsConstraints/' + str(minWm)))
        print('- Assign Min Threads Constraint : ' + minWm)
      else:
        print('- Min Threads Constaint ' + minWm + ' Not Found')

    if reqClass == "None":
      cd('/SelfTuning/' + domainName + '/WorkManagers/' + str(wmName))
      cmo.setFairShareRequestClass(None)
      cmo.setContextRequestClass(None)
      cmo.setResponseTimeRequestClass(None)

    else:
      exRes = ls('/SelfTuning/' + domainName + '/ResponseTimeRequestClasses/', returnMap='true')
      exFair = ls('/SelfTuning/' + domainName + '/FairShareRequestClasses/', returnMap='true')
      exCon = ls('/SelfTuning/' + domainName + '/ContextRequestClasses/', returnMap='true')

      if reqClass in exRes:
        cd('/SelfTuning/' + domainName + '/WorkManagers/' + str(wmName))
        cmo.setResponseTimeRequestClass(getMBean('/SelfTuning/' + domainName + '/ResponseTimeRequestClasses/' + str(reqClass)))
        cmo.setFairShareRequestClass(None)
        cmo.setContextRequestClass(None)
        print('- Assign Response Time Request Class : ' + reqClass)
      
      if reqClass in exFair:
        cmo.setFairShareRequestClass(getMBean('/SelfTuning/' + domainName + '/FairShareRequestClasses/' + str(reqClass)))
        cmo.setResponseTimeRequestClass(None)
        cmo.setContextRequestClass(None)
        print('- Assign Fair Share Request Class : ' + reqClass)

      if reqClass in exCon:
        cmo.setContextRequestClass(getMBean('/SelfTuning/' + domainName + '/ContextRequestClasses/' + str(reqClass)))
        cmo.setFairShareRequestClass(None)
        cmo.setResponseTimeRequestClass(None)
        print('- Assign Context Request Class : ' + reqClass)

    if Capacity != "None":
      cmo.setCapacity(getMBean('/SelfTuning/' + domainName + '/Capacities/' + str(Capacity)))
      #cmo.setIgnoreStuckThreads(false)

    # Target to server/cluster
    cd('/SelfTuning/' + domainName + '/WorkManagers/' + str(wmName))
    target(serverTarget)
    #set('Targets',jarray.array(targetsForDeployment, ObjectName))

  except Exception, e:
    print e
	
def main():
  propInputStream = FileInputStream(sys.argv[1])
  configProps = Properties()
  configProps.load(propInputStream)
   
  url=configProps.get("adminUrl")
  username=configProps.get("importUser")
  password=configProps.get("importPassword")
  csvLoc=configProps.get("csvLoc")
  
  connect(username , password , url)
  edit()
  file=open(csvLoc)
  for line in file.readlines():
    if line.strip().startswith('minThreadCon'):
      createMinWM(line)
    elif line.strip().startswith('maxThreadCon'):
      createMaxWM(line)
    elif line.strip().startswith('capacityConstraint'):
      createCapacity(line)
    elif line.strip().startswith('resTimeReqClass'):
      createResTimeReqClass(line)
    elif line.strip().startswith('fairShareReqClass'):
      createFairShareReqClass(line)
    elif line.strip().startswith('conReqClass'):
      createConReqClass(line)
    elif line.strip().startswith('workManager'):
      createWorkManager(line)
    else:
      continue

  save()
  activate()
	
  disconnect()

main()
	
