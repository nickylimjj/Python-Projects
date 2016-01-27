
def deuce(p1,p2):
    seq = ''
    while True:
        if p1[0]*2 in seq or p2[0]*2 in seq: #a player won twice in a row
            break
        winner = raw_input('who won this deuce point? ({}/{})'.format(p1,p2))
        

        if winner.lower() == p1[0]:
            seq += p1[0]
            print "adv - 40"
        elif winner.lower() == p2[0]:
            seq += p2[0]
            print "40 - adv"
         
    if p1[0]*2 in seq:
        return p1
    if p2[0]*2 in seq:
        return p2
        
def game(p1,p2):
    game= {
    0: 'love',
    1: '15',
    2: '30',
    3: '40',
    4: 'game',
    888: 'adv'
}
    p1_score = 0
    p2_score = 0
    while True:
        if game[p1_score] == 'game' or game[p2_score] == 'game': #exit loop once someone won gamepoint
            break
        if game[p1_score] == '40' and game[p2_score] == '40': #exit loop once someone won gamepoint
            print 'deuce entered'
            
        if p1_score == 3 and p2_score == 3: #deuce
            deuce_results = deuce(p1,p2)
            if deuce_results == p1:
                p1_score = 4
            elif deuce_results == p2:
                p2_score = 4
            
        else: #normal gameplay
            point = raw_input("Who scored? ({}/{}):".format(p1,p2)) 
            assert point == p1[0] or p2[0]
            if point.lower() == p1[0]:
                p1_score += 1
                print "{} - {} ".format(game[p1_score],game[p2_score])
            elif point.lower() == p2[0]:
                p2_score +=1
                print "{} - {} ".format(game[p1_score],game[p2_score])
            

    if p1_score > p2_score:
        print '{} takes this game'.format(p1)
        return p1
    else:
        print '{} takes this game'.format(p2)
        return p2

def deuce_set(p1,p2,set_score):
    p1_count = set_score[0]
    p2_count = set_score[1]
    while True:
        if abs(p1_count - p2_count) >= 2: #a player is two games up
            break
            
        game_winner = game(p1,p2)
        
        if game_winner == p1:
            p1_count += 1
            
        elif game_winner == p2:
            p2_count +=1
         
        score = [p1_count,p2_count]
    if p1_count > p2_count:
        return [p1,score]
    if p2_count > p1_count:
        return [p2,score]

def set(game,p1,p2):
    p1_set_score = 0
    p2_set_score = 0
    set_score = [p1_set_score,p2_set_score]
    games_to_win_set = 2
    set_number = 0
    
    print "first to {}." .format(games_to_win_set)
    
    while True:
        
        print "set {}: " .format(set_number+1), "score: {} - {}" .format(set_score[0],set_score[1]) #tracker
        
        if p1_set_score == games_to_win_set or p2_set_score == games_to_win_set:
            break    
            
        if p1_set_score == games_to_win_set-1 and p2_set_score == games_to_win_set-1: #enter deuce
            print 'enter deuce set'
            deuce_results =deuce_set(p1,p2,set_score)
            set_score = deuce_results[1]
            
            if deuce_results[0] == p1:
                p1_set_score+=1
            if deuce_results[0] == p2:
                p2_set_score +=1                
            break        
                           
        game_won = game(p1,p2)
        
        if game_won == p1:
            p1_set_score +=1
        if game_won == p2:
            p2_set_score +=1
        set_score = [p1_set_score,p2_set_score]
        set_number += 1        

    
    if p1_set_score > p2_set_score:
        print "{} wins this set! Score: {} - {}" .format(p1,set_score[0],set_score[1])
    else:
        print "{} wins this set! Score: {} - {}" .format(p2,set_score[0],set_score[1])           



set(game,'dongxing','yuhan')