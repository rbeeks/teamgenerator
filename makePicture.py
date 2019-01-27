import os, random
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from math import pi

def makeChart(skill_avg, fig, c, save_name):

    categories=["Shooting","Passing","Defending","Goalkeeping","Fitness"]
    N = len(categories)

    skill_avg += skill_avg[:1]

    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    plt.figure(fig)
    ax = plt.subplot(111, polar=True)

    plt.xticks(angles[:-1], categories, color='grey', size=24)

    i=0
    for label in ax.get_xticklabels():
        label.set_rotation(angles[i]*180/pi - 90)
        i+=1

    ax.set_rlabel_position(0)
    plt.yticks([5,10,15], ["5","10","15"], color="grey", size=17)
    plt.ylim(0,20)

    ax.plot(angles, skill_avg, color=c, linewidth=1, linestyle='solid')

    ax.fill(angles, skill_avg, color=c, alpha=0.1)

    plt.savefig(save_name)

    return True

def selectRandomLogo(folder):
    return random.choice([x for x in os.listdir(folder) if os.path.isfile(os.path.join(folder, x))])

def makePicture(team1, team2, save_name):
    path1, path2 = './data/' + selectRandomLogo('./data/'), './data/' + selectRandomLogo('./data/')

    logo1, logo2 = Image.open(path1, 'r'), Image.open(path2, 'r')

    w1, h1 = logo1.size
    w2, h2 = logo2.size

    makeChart(team1.get_skill_avg(), 1, 'b', 'chart1.png')
    makeChart(team2.get_skill_avg(), 2, 'r', 'chart2.png')

    chart1, chart2 = Image.open('chart1.png', 'r'), Image.open('chart2.png', 'r')

    w3, h3 = chart1.size
    w4, h4 = chart2.size

    resize_ratio = float(w3)/float(w1)

    w1, h1, w2, h2 = [int(x * resize_ratio) for x in [w1, h1, w2, h2]]

    logo1 = logo1.resize((w1, h2), Image.ANTIALIAS)
    logo2 = logo2.resize((w2, h2), Image.ANTIALIAS)

    gap = w1/2
    name_offset = 100

    img = Image.new('RGBA', (w1 + w2 + gap, h1 + 1200), (255, 255, 255, 255))

    img.paste(logo1, (0, 0))
    img.paste(logo2, (w1 + gap, 0))
    img.paste(chart1, ((w1 - w3)/2 - name_offset, h1 + 150))
    img.paste(chart2, (w1 + gap + (w2 - w4)/2 + name_offset, h2 + 150))

    fnt = ImageFont.truetype('./roboto/Roboto-Regular.ttf', 60)
    d = ImageDraw.Draw(img)

    w5, h5 = d.textsize(team1.name, font=fnt)
    w6, h6 = d.textsize(team2.name, font=fnt)
    d.text(((w1 - w5)/2, h1 + 10), team1.name, font=fnt, fill=(0, 0, 0))
    d.text((w1 + gap + (w2 - w6)/2, h2 + 10), team2.name, font=fnt, fill=(0, 0, 0))

    fnt = ImageFont.truetype('./roboto/Roboto-Regular.ttf', 40)
    i=0
    for player in team1.players:
        w_player, h_player = d.textsize(player.name, font=fnt)
        d.text(((w1 + w3)/2 - name_offset, h1 + 200 + i), player.name, font=fnt, fill=(0,0,0))
        i += 50
    i=0
    for player in team2.players:
        w_player, h_player = d.textsize(player.name, font=fnt)
        d.text((w1 + gap + 10, h2 + 200 + i), player.name, font=fnt, fill=(0,0,0))
        i += 50 

    fnt = ImageFont.truetype('./roboto/Roboto-Regular.ttf', 180)
    d.text((w1 + 100, h1 - 50), "VS", font=fnt, fill=(0,0,0))

    img.save(save_name)
    
    return True
