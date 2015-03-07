0 High Card: Highest value card.
1 One Pair: Two cards of the same value.
2 Two Pairs: Two different pairs.
3 Three of a Kind: Three cards of the same value.
4 Straight: All cards are consecutive values.
5 Flush: All cards of the same suit.
6 Full House: Three of a kind and a pair.
7 Four of a Kind: Four cards of the same value.
8 Straight Flush: All cards are consecutive values of same suit.
9 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.


cardRanks = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, 
             '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 
             'Q': 10, 'K': 11, 'A': 12}


def faces(hand) :
  return [i[0] for i in hand]


def suits(hand) :
  return [i[1] for i in hand]


def straight(hand, royal = False) :
  cards = [cardRanks[i] for i in faces(hand)]
  cards.sort()
  #print cards
  last = cards[0]
  for card in cards[1:] :
    #print "%d - %d = %d" % (card, last, card - last)
    if card - last != 1 : return False
    last = card
  return not royal or cards[0] == 8


def flush(hand) :
  cards = suits(hand)
  return cards.count(cards[0]) == 5


def freqs(hand) :
  faceList = faces(hand)
  return [faceList.count(i) for i in faceList]


def pairs(freqCount) :
  return freqCount.count(2)/2


def handRank(hand) :
  isFlush = flush(hand)
  isStraight = straight(hand, True)
  if isFlush and isStraight : return 9
  isStraight = straight(hand)
  if isFlush and isStraight : return 8
  freqCounts = freqs(hand)
  if 4 in freqCounts : return 7
  if 2 in freqCounts and 3 in freqCounts : return 6
  if isFlush : return 5
  if isStraight : return 4
  if 3 in freqCounts : return 3
  pairCount = pairs(freqCounts)
  return pairCount


def highFullHouse(hand) :
  faceList = faces(hand)
  return faceList[freqs(hand).index(3)]


def highPair(hand) :
  faceList = faces(hand)
  freqList = freqs(hand)
  return max([faceList[i] for i in range(0,5) if freqList[i] == 2])


def highCard(one, two) :
  rankOne = [cardRanks[i] for i in faces(one)]
  rankTwo = [cardRanks[i] for i in faces(two)]
  rankOne.sort()
  rankTwo.sort()
  i = 4
  while i > 0 and rankOne[i] == rankTwo[i] : i -= 1
  return rankOne[i] > rankTwo[i]


def splitHand(hand) :
  return hand.split(' ')


def handWins(one, two) :
  handOne = handRank(one)
  handTwo = handRank(two)
  if handOne != handTwo :
    return handOne > handTwo
  if handOne == 6 :
    oneRank = cardRanks[highFullHouse(one)]
    twoRank = cardRanks[highFullHouse(two)]
    if oneRank != twoRank :
      return oneRank > twoRank 
  if handOne == 2 or handOne == 1 :
    oneRank = cardRanks[highPair(one)]
    twoRank = cardRanks[highPair(two)]
    if oneRank != twoRank :
      return oneRank > twoRank 
  print "Tied %d! %s %s" % (handOne, ' '.join(one), ' '.join(two)[:-1])
  return highCard(one, two)


poker = open("poker.txt")
sum(handWins(splitHand(hand[:14]), splitHand(hand[15:])) for hand in poker)
poker.close()


2H 2D 4C 4D 4S 3C 3D 3S 9S 9D
