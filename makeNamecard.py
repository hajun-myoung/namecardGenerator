from PIL import ImageFont, ImageDraw, Image
import cv2
import os
import numpy as np

# 3126 * 4689

def validatePath():
    requiredDirectories = ["data", "fonts", "namecards", "tools"]
    for dir in requiredDirectories:
        isExist = os.path.isdir(dir)
        if not isExist:
            print(f"It looks like there is no {dir} in your root directory")
            os.mkdir(dir, mode=0o777)
        else:
            print(f"[INFO]\t{dir} dir existence check ... success ✔")

def main():
    validatePath()

    dataSourcePath = "./data"
    fontPath = "./fonts"
    fontName = "BMDOHYEON_ttf.ttf"

    outPath = "./namecards"
    # outPath = "./additionalNamecards"

    textFilename = "participants.txt"
    # textFilename = "addition.txt"
    participants = []
    with open(f"{dataSourcePath}/{textFilename}", "+r") as f:
        for line in f:
            # print(line.split("\t"))
            team, name, role, isTeacher, bod = line.split(",")
            try:
                team = int(team)
            except Exception as e:
                print(e)
            if bod.endswith("\n"):
                bod = bod[:-1]
            participants.append((team, name, role, isTeacher, bod))
            
        f.close()
    
    bods = ["99또래", "98또래", "97또래", "00또래", "01또래"]
    roles = ["선생님", "간사님", "목사님", "전도사님", "스태프"]
    grades = ["예시1", "예시2", "예시3", "예시4", "예시5", "예시6"]

    # images = ["아무개_년생_아이디.png"]
    
    for curPerson in participants:
        print(curPerson)
        team, name, role, isTeacher, bod = curPerson
        
        print(f"{name} 명찰을 만들기 시작합니다")
        print(bod)

        backgroundFilename = ["background.jpg", "backgroundB.jpg"]
        if role in roles:
            background = cv2.imread(f"{dataSourcePath}/{backgroundFilename[1]}")
            grade = bod
            textColor = (156, 134, 212, 1)
        elif bod == "깍두기":
            background = cv2.imread(f"{dataSourcePath}/{backgroundFilename[0]}")
            grade = bod
            textColor = (117, 53, 78, 1)
        else:
            background = cv2.imread(f"{dataSourcePath}/{backgroundFilename[0]}")
            indexOfBod = bods.index(bod)
            grade = grades[indexOfBod]
            textColor = (117, 53, 78, 1)

        textImage = np.zeros((4689, 3126, 3), dtype="uint8")
        textImage[:, :] = background

        font = ImageFont.truetype(f"{fontPath}/{fontName}", 800 if len(name) <= 3 else 720)
        smallFont = ImageFont.truetype(f"{fontPath}/{fontName}", 240)
        superSmallFont = ImageFont.truetype(f"{fontPath}/{fontName}", 200)
        
        textImage_PIL = Image.fromarray(textImage)
        draw = ImageDraw.Draw(textImage_PIL)

        x0 = 200 if len(name) > 2 else 450
        y0 = 1200

        xLen = 2000 if len(name) > 2 else 1450
        xGap = int(xLen / (len(name) - 1 ))

        for idx, char in enumerate(name):
            draw.text((x0 + idx * xGap, 1200), char, font=font, fill=textColor)
        
        teamText = f"{team}조" if team > 0 else ""
        draw.text((1400, 2200), teamText, font=smallFont, fill=textColor)
        
        if grade in ["선생님", "목사님", "간사님", "깍두기"]:
            draw.text((2350, 2225), grade, font=superSmallFont, fill=textColor)
        elif grade == "전도사님":
            draw.text((2250, 2225), grade, font=superSmallFont, fill=textColor)
        else:
            draw.text((2500, 2225), grade, font=superSmallFont, fill=textColor)

        newImage = np.array(textImage_PIL)
        
        # cv2.imshow("image", newImage)
        # cv2.waitKey()
        cv2.imwrite(f"{outPath}/{name}.png", newImage)
        print("")

    print("명찰이 모두 생성되었습니다!")
    return True

if __name__ == "__main__":
    main()