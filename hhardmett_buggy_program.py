#Howard Hardnett
#03/02/2022
#Assignment 11
# The purpose of this assignment is to create a bug and see if my classmates can find the error.

from sys import displayhook


bodybuilding = {
	'food':'I like bodybuilding becuase I like to eat. Even though the food is clean, you can still enjoy it and use it as fuel.',
	'lifting':'I like lifting because I enjoy getting stronger.',
	'competing':'I can step on stage and win competitions.',
	'lifestyle':'Everything I do is structured so the bodybuilding lifestyle comes natural to me.',
	'friendships':'I have the opportuninty to meet some great people throuhout the world because we all share a common goal.',
	'give back':'Now that I have been competing for a while and I understand nutrition, I can help people achieve their own health goals.',
	'physical changes':'What the human body can do is amazing so to see myself go from one look to another in a matter of months is just awesome to witness.',
	'patience':'Bodybuilding teaches patience becuase you cannot just train and get big or train and lose weight overnight, it all takes time.',
	'discipline':'Bodybuilding teaches discipline becuase when you are prepping for a show, you have to stick to the meal plan and not deviate from it.',
	'fun':'I simply like bodybuilding because I enjoy training, eating, sleeping, and competing.'
}


def greeting():
	print('The topic that interest me is bodybuilding.')
	print('In the textbox below please enter in one of the sub topics to know why I enjoy bodybuilding.')


def get_keys():
	for x in bodybuilding:
		print(x) #Shows all of the keys to the user.

def Display(): #using this command so I can run it again if the user is not done looking at the sub topics . 
	reasons=(input('Please select enter in an value: '))
	reason = bodybuilding.get(reasons)
	if reason and bodybuilding:
		print(bodybuilding[reasons])
		finished()
	elif reasons == 'exit' or reasons == 'Exit':
		finished()
	else:
		print('The option you entered is not on the list.')
		Display()
  
def finished():
	done=(input('Are you done? ')).lower()
	if done =='yes':
		close=(input('press enter to close'))
	else:
		get_keys()
		Display()

def main():
    greeting()
    get_keys()
    Display()
    
main()