import json
from collections import OrderedDict

SM_RIGHT_IDLE  = [[277,59,12,15]]
SM_RIGHT_RUN = [[292,59,12,14],[307,59,11,15],[321,59,15,15]]
SM_RIGHT_JUMP = [[355,61,16,17]]
SM_RIGHT_DEATH = [[486,60,14,14]]

SM_LEFT_IDLE = [[224,59,12,15] ]
SM_LEFT_RUN = [ [209,59,12,14],[195,59,11,15],[177,59,15,15]]
SM_LEFT_JUMP = [[142,61,16,17]]
SM_LEFT_DEATH = [[13,60,14,14] ]


BM_RIGHT_IDLE  = [[258,49,16,48]]
BM_RIGHT_RUN = [[296,47,16,44],[316,48,13,46],[331,48,16,47]]
BM_RIGHT_JUMP = [[369,50,16,49]]


BM_LEFT_IDLE = [[239, 49, 16, 48] ]
BM_LEFT_RUN = [[202, 47, 16, 44],[185, 48, 13, 46],[166, 48, 16, 47]]
BM_LEFT_JUMP = [[128, 50, 16, 49]]


MONSTER1_MOVE = [[296, 204, 16, 17],[315, 204, 16, 17]]
MONSTER1_DEATH = [[277, 204, 16, 9]]

MONSTER2_RIGHT_MOVE = [[296, 237, 16, 29],[315, 237, 16, 29]]
MONSTER2_LEFT_MOVE = [[201, 237, 16, 29],[182, 237, 16, 29]]




file_data = OrderedDict()

file_data["SMALLMARIO"] = {
    "RIGHT_IDLE": {
        "FRAMESIZE" : len(SM_RIGHT_IDLE),
    "FRAMES": {str(i) : {"LEFT": list[0], "BOTTOM" : 401-list[1],"WIDTH":list[2],"HEIGHT": list[3]}  for i, list in enumerate(SM_RIGHT_IDLE)}
                   },


    "RIGHT_RUN": {        "FRAMESIZE" : len(SM_RIGHT_RUN),
    "FRAMES": {str(i) : {"LEFT": list[0], "BOTTOM" : 401-list[1],"WIDTH":list[2],"HEIGHT": list[3]}  for i, list in enumerate(SM_RIGHT_RUN)}
                   },

    "RIGHT_JUMP": {"FRAMESIZE": len(SM_RIGHT_JUMP),
                  "FRAMES": {
                      str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]}
                      for i, list in enumerate(SM_RIGHT_JUMP)}
                  },

    "RIGHT_DEATH": {"FRAMESIZE": len(SM_RIGHT_DEATH),
                  "FRAMES": {
                      str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]}
                      for i, list in enumerate(SM_RIGHT_DEATH)}
                  },
    "LEFT_IDLE": {
        "FRAMESIZE": len(SM_LEFT_IDLE),
        "FRAMES": {str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]} for
                   i, list in enumerate(SM_LEFT_IDLE)}
    },

    "LEFT_RUN": {"FRAMESIZE": len(SM_LEFT_RUN),
                  "FRAMES": {
                      str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]}
                      for i, list in enumerate(SM_LEFT_RUN)}
                  },

    "LEFT_JUMP": {"FRAMESIZE": len(SM_LEFT_JUMP),
                   "FRAMES": {
                       str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]}
                       for i, list in enumerate(SM_LEFT_JUMP)}
                   },

    "LEFT_DEATH": {"FRAMESIZE": len(SM_LEFT_DEATH),
                    "FRAMES": {
                        str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]}
                        for i, list in enumerate(SM_LEFT_DEATH)}
                    },
    }

file_data["BIGMARIO"] = {
    "RIGHT_IDLE": {
        "FRAMESIZE" : len(BM_RIGHT_IDLE),
    "FRAMES": {str(i) : {"LEFT": list[0], "BOTTOM" : 401-list[1],"WIDTH":list[2],"HEIGHT": list[3]}  for i, list in enumerate(BM_RIGHT_IDLE)}
                   },


    "RIGHT_RUN": {        "FRAMESIZE" : len(BM_RIGHT_RUN),
    "FRAMES": {str(i) : {"LEFT": list[0], "BOTTOM" : 401-list[1],"WIDTH":list[2],"HEIGHT": list[3]}  for i, list in enumerate(BM_RIGHT_RUN)}
                   },

    "RIGHT_JUMP": {"FRAMESIZE": len(BM_RIGHT_JUMP),
                  "FRAMES": {
                      str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]}
                      for i, list in enumerate(BM_RIGHT_JUMP)}
                  },
    "LEFT_IDLE": {
        "FRAMESIZE": len(BM_LEFT_IDLE),
        "FRAMES": {str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]} for
                   i, list in enumerate(BM_LEFT_IDLE)}
    },

    "LEFT_RUN": {"FRAMESIZE": len(BM_LEFT_RUN),
                 "FRAMES": {
                     str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]}
                     for i, list in enumerate(BM_LEFT_RUN)}
                 },

    "LEFT_JUMP": {"FRAMESIZE": len(BM_LEFT_JUMP),
                  "FRAMES": {
                      str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]}
                      for i, list in enumerate(BM_LEFT_JUMP)}
                  },

    }

file_data["MONSTER1"] = {
    "MOVE": {"FRAMESIZE": len(MONSTER1_MOVE),
                  "FRAMES": {
                      str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]}
                      for i, list in enumerate(MONSTER1_MOVE)}
                  },
    "DEATH": {"FRAMESIZE": len(MONSTER1_DEATH),
                   "FRAMES": {
                       str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]}
                       for i, list in enumerate(MONSTER1_DEATH)}
                   },


}

file_data["MONSTER2"] = {
    "RIGHT_MOVE": {"FRAMESIZE": len(MONSTER2_RIGHT_MOVE),
             "FRAMES": {
                 str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]}
                 for i, list in enumerate(MONSTER2_RIGHT_MOVE)}
             },
    "LEFT_MOVE": {"FRAMESIZE": len(MONSTER2_LEFT_MOVE),
              "FRAMES": {
                  str(i): {"LEFT": list[0], "BOTTOM": 401-list[1], "WIDTH": list[2], "HEIGHT": list[3]}
                  for i, list in enumerate(MONSTER2_LEFT_MOVE)}
              },

}



print(json.dumps(file_data, ensure_ascii= False, indent = "\t"))

with open("characters.json", 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")