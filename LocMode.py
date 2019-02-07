import maya.cmds as mc
import sys

def setLoc():
    if mc.objExists("locatorGrp")==True:
        sys.stderr.write('*****Error! Locator already exists!*****')
    else:
        # LocatorGrp
        mc.group(em=True,n="locatorGrp")

        # mainJoint
        mc.spaceLocator(a=True,n="hip",p=(1,93,-0.5))
        mc.spaceLocator(a=True,n="spineA",p=(1,107,2.5))
        mc.spaceLocator(a=True,n="spineB",p=(1,118,1.5))
        mc.spaceLocator(a=True,n="chest",p=(1,137,-1.4))
        mc.spaceLocator(a=True,n="neck",p=(1,157,-2.1))
        mc.spaceLocator(a=True,n="head",p=(1,164,0.3))
        mc.spaceLocator(a=True,n="headTop",p=(1,181,1))

        # leftLegJoint
        mc.spaceLocator(a=True,n="leftUpLeg",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftLeg",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftFoot",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftToe",p=(1,1,1))

        # leftArmJoint
        mc.spaceLocator(a=True,n="leftClavicle",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftArm",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftForeArm",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftWrist",p=(1,1,1))

        # leftHandJoint
        mc.spaceLocator(a=True,n="leftHandThumbA",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandThumbB",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandThumbC",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandThumbD",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandIndexA",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandIndexB",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandIndexC",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandIndexD",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandMiddleA",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandMiddleB",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandMiddleC",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandMiddleD",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandRingA",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandRingB",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandRingC",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandRingD",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandPinkyA",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandPinkyB",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandPinkyC",p=(1,1,1))
        mc.spaceLocator(a=True,n="leftHandPinkyD",p=(1,1,1))



        # rightLegJoint
        mc.spaceLocator(a=True,n="rightUpLeg",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightLeg",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightFoot",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightToe",p=(1,1,1))

        # rightArmJoint
        mc.spaceLocator(a=True,n="rightClavicle",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightArm",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightForeArm",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightWrist",p=(1,1,1))

        # rightHandJoint
        mc.spaceLocator(a=True,n="rightHandThumbA",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandThumbB",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandThumbC",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandThumbD",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandIndexA",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandIndexB",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandIndexC",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandIndexD",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandMiddleA",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandMiddleB",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandMiddleC",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandMiddleD",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandRingA",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandRingB",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandRingC",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandRingD",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandPinkyA",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandPinkyB",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandPinkyC",p=(1,1,1))
        mc.spaceLocator(a=True,n="rightHandPinkyD",p=(1,1,1))

        # parentLocator
        mc.parent('hip','spineA','spineB','chest','neck','head','headTop','locatorGrp')

        mc.parent('leftUpLeg','leftLeg','leftFoot','leftToe','locatorGrp')
        mc.parent('leftClavicle','leftArm','leftForeArm','leftWrist','locatorGrp')
        mc.parent('leftHandThumbA','leftHandThumbB','leftHandThumbC','leftHandThumbD','locatorGrp')
        mc.parent('leftHandIndexA','leftHandIndexB','leftHandIndexC','leftHandIndexD','locatorGrp')
        mc.parent('leftHandMiddleA','leftHandMiddleB','leftHandMiddleC','leftHandMiddleD','locatorGrp')
        mc.parent('leftHandRingA','leftHandRingB','leftHandRingC','leftHandRingD','locatorGrp')
        mc.parent('leftHandPinkyA','leftHandPinkyB','leftHandPinkyC','leftHandPinkyD','locatorGrp')

        mc.parent('rightUpLeg','rightLeg','rightFoot','rightToe','locatorGrp')
        mc.parent('rightClavicle','rightArm','rightForeArm','rightWrist','locatorGrp')
        mc.parent('rightHandThumbA','rightHandThumbB','rightHandThumbC','rightHandThumbD','locatorGrp')
        mc.parent('rightHandIndexA','rightHandIndexB','rightHandIndexC','rightHandIndexD','locatorGrp')
        mc.parent('rightHandMiddleA','rightHandMiddleB','rightHandMiddleC','rightHandMiddleD','locatorGrp')
        mc.parent('rightHandRingA','rightHandRingB','rightHandRingC','rightHandRingD','locatorGrp')
        mc.parent('rightHandPinkyA','rightHandPinkyB','rightHandPinkyC','rightHandPinkyD','locatorGrp')

setLoc()
