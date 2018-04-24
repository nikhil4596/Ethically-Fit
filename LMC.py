from flask import Flask, render_template, request
import numpy as np

outfile = "C:\\Users\\nikhil\\Desktop\LMC\static\\file.npz"
file = np.load(outfile)
answers = file["data"].item()
# majors = set([m.decode('UTF-8') for m in ms])
scenarios = [
    "Tim is a doctor at a top hospital. Tim has six gravely ill patients, five of whom are in urgent need of organ transplants. Tim can't help them, though, because there are no available organs that can be used to save their lives. The sixth patient, however, will die without a particular medicine. If s/he dies, Tim will be able to save the other five patients by using the organs of patient 6, who is an organ donor. Tim decides to cure the 6th ailing person by giving her/him the required medicine but in the process the rest 5 die due to lack of organs. Was Tim decision ethical?",
    "There are 3 friends Tony, Jim and Mark. They are all in the same LMC class. Jim did not finish his essay on time and was very stressed. Tony jokingly told Jim to cheat from Mark's essay and Jim actually ended up cheating from Mark's essay. Now, unknown to Tony, Jim had already been thinking about plagiarizing Mark's essay and would have done it anyways. In this situation, was Tony ethical or unethical?",
    "Billy is an eyewitness to a crime: A man has robbed a bank, but instead of keeping the money for himself, he donates it to a poor orphanage that can now afford to feed, clothe, and care for its children. Billy knows who committed the crime. If billy goes to the authorities with the information, there's a good chance the money will be returned to the bank, leaving a lot of kids in need. Billy decided to ignore what he saw and leave. Was what billy did ethical or unethical?",
    "Roy was on a cruise for two days when there's an accident that forced everyone on board to abandon ship. During the evacuation, one of the boats is damaged, leaving it with a hole that fills it with water. Roy figures that with 10 people in the boat, he can keep the boat afloat by having nine people scoop the filling water out by hand for 10 minutes while the 10th person rests. After that person's 10-minute rest, he or she will get back to work while another person rests, and so on. This should keep the boat from sinking long enough for a rescue team to find them as long as it happens within five hours. Roy is taking his first brake when he notices his best friend in a sound lifeboat with only nine people in it and he beckons him to swim over and join them so he won't have to keep bailing out water. If he leaves the people in the sinking boat, they will only be able to stay afloat for two hours instead of five, decreasing their chance of being rescued, but securing roys. Roy decided to leave the boat. Was it ethical or unethical",
    "A distressed man, who has threatened to explode several bombs in crowded areas, has been apprehended. Unfortunately, he has already planted the bombs and they are scheduled to go off in a short time. It is possible that hundreds of people may die. The authorities cannot make him divulge the location of the bombs by conventional methods. He refuses to say anything and requests a lawyer to protect his fifth amendment right against self-incrimination. In exasperation, some high level official suggests forceful measures like torture etc. against this man and his faimly to make him talk. This is definitely illegal, of course, but the official thinks that it is nevertheless the right thing to do in this desperate situation. Is the officer's thinking ethical",
    "Tom is part of a group of ecologists who live in a remote stretch of jungle. The entire group, which includes eight children, has been taken hostage by a group of paramilitary terrorists. One of the terrorists takes a liking to Tom. He informs Tom that his leader intends to kill him and the rest of the hostages the following morning. He is willing to help Tom and the children escape, but as an act of good faith he wants Tom to torture and kill one of his fellow hostages whom he does not like. If Tom refuses his offer, all the hostages including the children and Tom will die. If he accepts his offer, then the others will die in the morning but Tom and the eight children will escape. Tom decided to not to use power to torture and rejected his offer and thus, was responsible for deaths of everyone including his own. Was Tom ethical in his decision",
    "Austin is a single father of three young girls, He has always been the cool dad but lately all his kids have been acting a bit strange. He isn't sure if his daughters are involved with some bad substances or if it is the teenage that is making them like this. He has been getting very worried about this and thus troubled, he decides to snoop around and check one of his daughter's laptop. He searches around a bit but doesn't find any proof that she is troubled. He didnt find anything to validate his doubts but came across some very private though unrelated conversation of his daughter with her friend that she  would never have shared with anyone else. Was Austin ethical in his decision to confirm his doubts and caring for his children?"]

#answers = {
#    'Computer Sci': [{'e': 18, 'u': 12}, {'e': 11, 'u': 19}, {'e': 4, 'u': 26}, {'e': 20, 'u': 10}, {'e': 0, 'u': 30},
#                     {'e': 10, 'u': 20}, {'e': 25, 'u': 15}],
#    'Life Sciences': [{'e': 12, 'u': 18}, {'e': 4, 'u': 26}, {'e': 0, 'u': 30}, {'e': 10, 'u': 20}, {'e': 0, 'u': 30},
#                      {'e': 20, 'u': 10}, {'e': 13, 'u': 17}],
#    'Advertisement': [{'e': 3, 'u': 1}, {'e': 1, 'u': 3}, {'e': 2, 'u': 2}, {'e': 3, 'u': 1}, {'e': 0, 'u': 4},
#                      {'e': 3, 'u': 1}, {'e': 1, 'u': 3}],
#    'Mechanical': [{'e': 13, 'u': 27}, {'e': 10, 'u': 30}, {'e': 20, 'u': 20}, {'e': 15, 'u': 25}, {'e': 10, 'u': 30},
#                   {'e': 19, 'u': 21}, {'e': 22, 'u': 18}],
#    'Law': [{'e': 5, 'u': 5}, {'e': 9, 'u': 1}, {'e': 7, 'u': 3}, {'e': 6, 'u': 4}, {'e': 5, 'u': 5}, {'e': 2, 'u': 8},
#            {'e': 6, 'u': 4}],
#    'Entertainment': [{'e': 4, 'u': 0}, {'e': 3, 'u': 1}, {'e': 2, 'u': 2}, {'e': 4, 'u': 0}, {'e': 3, 'u': 1},
#                      {'e': 1, 'u': 3}, {'e': 2, 'u': 2}],
#    'Business': [{'e': 20, 'u': 5}, {'e': 15, 'u': 10}, {'e': 10, 'u': 15}, {'e': 8, 'u': 17}, {'e': 16, 'u': 9},
#                 {'e': 20, 'u': 5}, {'e': 14, 'u': 11}]}

majors = set(answers.keys())

total_responses = {}
for mj in majors:
    total_responses[mj] = [0 for _ in range(len(scenarios))]
    for i in range(len(scenarios)):
        total_responses[mj][i] = answers[mj][i]['e'] + answers[mj][i]['u']

user_ans = []

app = Flask(__name__)


@app.route('/')
def index():
    print(majors)
    return render_template("index.html")


def score(ans, num):
    res = []
    for mj in majors:
        if total_responses[mj][num] != 0:
            val = answers[mj][num][ans]*1.0 / total_responses[mj][num] * 100
        if num > 1:
            val +=  answers[mj][num-1][ans]*1.0 / total_responses[mj][num-1] * 100
            val = val/2
            res.append((mj, round(float(val), 2)))
    res.sort(key=lambda x: x[1])
    res.reverse()
    print ("RES", res)
    return res


@app.route('/survey/')
def survey():
    params = request.args.get("params")
    major = params[6:]
    majors.add(major)
    num = int(request.args.get("num"))
    ans = int(request.args.get("ans"))
    if major not in answers.keys():
        answers[major] = [{'e': 0, 'u': 0} for _ in range(len(scenarios))]
        total_responses[major] = [0 for _ in range(len(scenarios))]
    out = [0 for _ in range(len(scenarios))]
    if num >= 0:
        if ans == 1:
            answers[major][num]['e'] += 1
            total_responses[major][num] += 1
            out = score('e', num)
        elif ans == 2:
            answers[major][num]['u'] += 1
            total_responses[major][num] += 1
            out = score('u', num)
    num = num + 1
    print("Answers", answers)
    if num >= len(scenarios):
        np.savez(outfile, data=answers)
        return render_template("end.html", out=out)
    return render_template("survey.html", num=num, scenario=scenarios[int(num)], maj=major, out=out)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
