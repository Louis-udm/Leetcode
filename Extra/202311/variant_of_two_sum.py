# Given a list of words L and a number N, 
# write a function that returns all words from "L" that 
# are of lenght "N" and are formed from two smaller words in "L".
# Example:
# N=6, L=["hot", "bird", "dog", "tailor", "hotdog", "or", "if", "tail"]
# Output: ["hotdog", "tailor"]
#
from collections import defaultdict

def combined_words(N: int, L: list[str]) -> list[str]:
    # Write your code here
    if not L or len(L)<2:
        return []
    if N<2:
        return []
    len_words=defaultdict(set)
    for w in L:
        w=w.strip()
        if w and len(w)<=N:
            len_words[len(w)].add(w)
    target_words=len_words.pop(N, None)
    if not target_words:
        return []
    
    results=set()
    while len(len_words)>0:
        i,words1=len_words.popitem()
        words1=list(words1)
        if N-i==i:
            for target in target_words:
                # for j,w1 in enumerate(words1[:-1]):
                for j,w1 in enumerate(words1):
                    if target.startswith(w1):
                        # 千万不要用if f"{w1}{w2}"==target or f"{w2}{w1}"==target
                        # 压力测试会超时
                        for w2 in words1:
                        # for w2 in words1[j+1:]:
                            if target.endswith(w2):
                                results.add(target)
                                # break
                    if target.endswith(w1):
                        for w2 in words1:
                        # for w2 in words1[j+1:]:
                            if target.startswith(w2):
                                results.add(target)
                                # break
        elif N-i in len_words:
            words2=list(len_words.pop(N-i))
            for target in target_words:
                for w1 in words1:
                    if target.startswith(w1):
                        for w2 in words2:
                            if target.endswith(w2):
                                results.add(target)
                                # break
                    if target.endswith(w1):
                        for w2 in words2:
                            if target.startswith(w2):
                                results.add(target)
                                # break
    return list(results)

print(combined_words(6, [" ", "permutations ","hot ", "bird", "dog", "tailor", "hotdog", "or", "if", "tail"]))
print(combined_words(6, ["","hot", "bird", "dog", "", "", "or", "if", "tail"]))
print(combined_words(6, ["","hot", "hotdog", "dog", "ho", "tdog"]))
print(combined_words(6, ["","hot", "hotdog", "dog", "ho", "tdog"]))
print(combined_words(6,["bye","byebye","ja","jajaja"]))


# cerence unit test cases
# 6
# ['hot', 'hot', 'dog', 'dog', 'hotdog']

# 7
# ['tailors', 'tail', 'ors']

# stress test
# 8
# ['species', 'practice', 'natural', 'measure', 'present', 'form', 'order', 'quality', 'condition', 'state', 'action', 'element', 'part', 'division', 'subject', 'ground', 'power', 'station', 'register', 'person', 'place', 'ordinary', 'strong', 'under', 'make', 'light', 'exercise', 'exchange', 'parallel', 'charge', 'support', 'judgment', 'substance', 'figure', 'strength', 'sound', 'service', 'quantity', 'standard', 'right', 'point', 'character', 'strike', 'discharge', 'force', 'return', 'spring', 'square', 'between', 'without', 'water', 'spirit', 'distance', 'contract', 'positive', 'position', 'straight', 'moderate', 'double', 'superior', 'certain', 'compound', 'interest', 'language', 'passage', 'business', 'through', 'manner', 'relation', 'general', 'process', 'strain', 'delicate', 'bearing', 'property', 'advance', 'account', 'original', 'religion', 'round', 'over', 'principal', 'sharp', 'surface', 'line', 'degree', 'report', 'course', 'matter', 'sentence', 'body', 'express', 'close', 'quarter', 'head', 'negative', 'take', 'plant', 'argument', 'increase', 'house', 'movement', 'table', 'balance', 'separate', 'small', 'back', 'entrance', 'settle', 'reason', 'machine', 'common', 'material', 'scale', 'authority', 'capable', 'anything', 'regular', 'stock', 'break', 'opposite', 'into', 'distress', 'work', 'standing', 'cross', 'color', 'number', 'stroke', 'convert', 'radical', 'relative', 'function', 'stand', 'press', 'question', 'peculiar', 'progress', 'together', 'touch', 'capacity', 'physical', 'horse', 'specific', 'external', 'produce', 'incapable', 'passion', 'represent', 'promise', 'tender', 'issue', 'family', 'range', 'domestic', 'shoulder', 'change', 'approach', 'transfer', 'carriage', 'feeling', 'security', 'something', 'direction', 'pressure', 'frame', 'like', 'free', 'company', 'inferior', 'distinct', 'variety', 'solution', 'capital', 'grain', 'deposit', 'circular', 'receive', 'pleasure', 'particular', 'office', 'faculty', 'motion', 'personal', 'country', 'narrow', 'occasion', 'open', 'addition', 'second', 'complete', 'short', 'ancient', 'contrary', 'serve', 'disorder', 'crown', 'mark', 'weight', 'large', 'white', 'tongue', 'mountain', 'address', 'vessel', 'throw', 'science', 'system', 'turn', 'object', 'temper', 'internal', 'base', 'pass', 'familiar', 'principle', 'another', 'that', 'hold', 'compass', 'pitch', 'influence', 'enter', 'command', 'reduce', 'level', 'surprise', 'time', 'bottom', 'face', 'flower', 'extreme', 'raise', 'purpose', 'nature', 'answer', 'down', 'against', 'stick', 'clear', 'record', 'article', 'discourse', 'string', 'shell', 'side', 'fall', 'backward', 'determine', 'several', 'forward', 'period', 'absolute', 'taste', 'draw', 'waste', 'running', 'spread', 'chamber', 'cause', 'official', 'province', 'flat', 'instrument', 'native', 'conduct', 'maintain', 'descent', 'block', 'presence', 'simple', 'lead', 'weather', 'direct', 'which', 'opinion', 'justice', 'guard', 'master', 'appearance', 'season', 'regard', 'check', 'shoot', 'society', 'liquid', 'rule', 'pattern', 'sphere', 'directly', 'cast', 'life', 'definite', 'private', 'give', 'knowledge', 'cover', 'weak', 'draught', 'section', 'sovereign', 'stop', 'organic', 'screw', 'violence', 'decision', 'render', 'beat', 'rise', 'current', 'affection', 'evidence', 'great', 'court', 'silver', 'hand', 'correct', 'roll', 'honor', 'wind', 'plate', 'channel', 'single', 'keep', 'heat', 'cylinder', 'divide', 'release', 'after', 'respect', 'military', 'stomach', 'some', 'root', 'timber', 'structure', 'school', 'exterior', 'syllable', 'piece', 'feather', 'pledge', 'supply', 'christian', 'branch', 'religious', 'necessary', 'father', 'execution', 'affected', 'knot', 'carry', 'other', 'circle', 'kind', 'worship', 'style', 'example', 'effect', 'obscure', 'well', 'violent', 'horn', 'english', 'drive', 'outside', 'better', 'church', 'mixture', 'with', 'equal', 'reproach', 'bear', 'volatile', 'equivalent', 'slender', 'remove', 'being', 'preserve', 'grace', 'earth', 'elevation', 'design', 'stream', 'furnish', 'dress', 'little', 'writing', 'spiritual', 'black', 'twist', 'picture', 'from', 'smooth', 'estate', 'fine', 'anchor', 'joint', 'heart', 'expression', 'reach', 'center', 'contest', 'trust', 'special', 'shall', 'friend', 'high', 'call', 'train', 'traverse', 'irregular', 'wrong', 'sign', 'watch', 'catch', 'animal', 'stone', 'dependent', 'before', 'relief', 'thought', 'fortune', 'will', 'active', 'formation', 'valuable', 'soft', 'about', 'operation', 'bank', 'heavy', 'solid', 'ring', 'proportion', 'symbol', 'opposition', 'apparent', 'abstract', 'portion', 'dignity', 'revolution', 'post', 'voluntary', 'length', 'market', 'harmony', 'prepare', 'perform', 'land', 'board', 'shaft', 'neglect', 'iron', 'value', 'attempt', 'hard', 'judge', 'proper', 'mouth', 'moral', 'district', 'interior', 'genus', 'union', 'purple', 'husband', 'wing', 'broken', 'foreign', 'divine', 'perfect', 'last', 'compact', 'escape', 'extract', 'demand', 'flexible', 'still', 'wheel', 'long', 'burden', 'labor', 'note', 'interval', 'column', 'destitute', 'reference', 'letter', 'control', 'freedom', 'swallow', 'medicine', 'history', 'difference', 'people', 'strip', 'contempt', 'handle', 'decline', 'good', 'liberty', 'brilliant', 'fashion', 'engage', 'rest', 'impression', 'offensive', 'drawing', 'purchase', 'minute', 'metal', 'texture', 'doctrine', 'cutting', 'lower', 'paper', 'sight', 'hollow', 'follow', 'judicial', 'formal', 'salt', 'blow', 'member', 'fellow', 'mean', 'mother', 'thread', 'corrupt', 'failure', 'associate', 'relieve', 'display', 'full', 'distant', 'disease', 'sense', 'liberal', 'intended', 'gather', 'play', 'blood', 'swell', 'stuff', 'bill', 'opening', 'quarrel', 'world', 'secure', 'stage', 'government', 'plane', 'public', 'composition', 'allowance', 'thing', 'establish', 'essential', 'gentle', 'consider', 'examine', 'attack', 'benefit', 'height', 'exhibit', 'movable', 'voice', 'tropical', 'platform', 'alternate', 'have', 'catholic', 'bound', 'advantage', 'bright', 'thrust', 'marble', 'mercury', 'alcohol', 'making', 'throat', 'foot', 'shelter', 'elastic', 'slight', 'painting', 'inclose', 'stem', 'reduction', 'vegetable', 'breast', 'drum', 'guide', 'generation', 'study', 'within', 'succession', 'dressing', 'powerful', 'staff', 'notice', 'downward', 'upright', 'favor', 'thick', 'trade', 'extend', 'custom', 'faith', 'mechanical', 'turning', 'front', 'agreement', 'glass', 'extension', 'normal', 'green', 'exposure', 'medium', 'product', 'application', 'term', 'vertical', 'shape', 'choice', 'more', 'somewhat', 'chance', 'result', 'residence', 'party', 'wear', 'confidence', 'soldier', 'continue', 'powder', 'found', 'learning', 'situation', 'bitter', 'struggle', 'finger', 'shield', 'officer', 'rough', 'field', 'space', 'privilege', 'delicacy', 'manifest', 'sacred', 'race', 'organ', 'behind', 'breath', 'belonging', 'phrase', 'border', 'marine', 'breathing', 'flesh', 'stretch', 'musical', 'imperfect', 'keeping', 'trouble', 'fresh', 'different', 'image', 'plaster', 'numerous', 'existence', 'surround', 'commerce', 'passing', 'rank', 'around', 'mill', 'popular', 'counter', 'fruit', 'praise', 'hence', 'beneath', 'loose', 'hammer', 'amount', 'pack', 'secondary', 'sweet', 'meeting', 'tone', 'inclined', 'refuse', 'game', 'floating', 'mineral', 'devotion', 'memory', 'individual', 'withdraw', 'size', 'severe', 'declare', 'warrant', 'desire', 'fish', 'provide', 'title', 'smoke', 'suffer', 'social', 'bond', 'virtue', 'doubtful', 'speech', 'sympathy', 'ready', 'feed', 'metallic', 'fast', 'step', 'leave', 'poison', 'worthy', 'entire', 'easily', 'steel', 'colored', 'disguise', 'variable', 'speaking', 'rising', 'indicate', 'band', 'primary', 'agitation', 'worm', 'quick', 'flight', 'discipline', 'careless', 'secret', 'lock', 'profession', 'affect', 'minister', 'excess', 'flourish', 'pole', 'tooth', 'situated', 'mind', 'disgrace', 'censure', 'estimate', 'treat', 'dead', 'chemical', 'grave', 'deliver', 'tail', 'drop', 'attention', 'surrender', 'hydrogen', 'american', 'sheet', 'building', 'preparation', 'attend', 'plain', 'fabric', 'limit', 'appear', 'fasten', 'bind', 'swelling', 'show', 'striking', 'witness', 'ornament', 'possession', 'bishop', 'name', 'collect', 'hinder', 'beyond', 'beginning', 'case', 'covenant', 'marriage', 'foul', 'yield', 'type', 'handsome', 'uniform', 'whatever', 'earnest', 'proof', 'himself', 'segment', 'former', 'critical', 'difficulty', 'proceed', 'walk', 'restrain', 'prince', 'setting', 'trick', 'leader', 'female', 'universal', 'floor', 'fire', 'false', 'depression', 'seal', 'class', 'similar', 'stamp', 'sleep', 'destroy', 'following', 'resemble', 'formerly', 'match', 'management', 'growth', 'suit', 'patient', 'aggregate', 'various', 'south', 'projection', 'habit', 'tissue', 'dispute', 'move', 'sacrifice', 'become', 'agreeable', 'credit', 'partial', 'chain', 'broad', 'northern', 'heavenly', 'pipe', 'arrangement', 'impulse', 'sport', 'apply', 'live', 'tension', 'write', 'above', 'wood', 'furnace', 'circuit', 'token', 'decree', 'trial', 'shade', 'child', 'engaged', 'imitation', 'meet', 'truth', 'fair', 'offer', 'supreme', 'constant', 'sensible', 'properly', 'share', 'device', 'pair', 'sugar', 'solemn', 'restore', 'commission', 'happiness', 'word', 'exact', 'criminal', 'model', 'belief', 'delivery', 'spot', 'suitable', 'commonly', 'ceremony', 'convey', 'search', 'behavior', 'printing', 'measured', 'frequent', 'ball', 'profit', 'especially', 'whole', 'admit', 'muscular', 'thin', 'singular', 'related', 'vapor', 'crowd', 'quiet', 'method', 'living', 'first', 'fault', 'skin', 'reverse', 'college', 'royal', 'chief', 'want', 'battle', 'appetite', 'disposition', 'recover', 'beam', 'drink', 'reverence', 'converse', 'essence', 'same', 'deprive', 'deep', 'nervous', 'wide', 'hawk', 'compose', 'skeleton', 'error', 'nucleus', 'proposition', 'bend', 'ship', 'drinking', 'difficult', 'whip', 'important', 'swimming', 'hanging', 'empty', 'wash', 'obligation', 'cotton', 'nerve', 'generally', 'prayer', 'century', 'view', 'servant', 'coloring', 'exertion', 'incline', 'unite', 'observation', 'middle', 'community', 'territory', 'bone', 'story', 'colorless', 'shallow', 'solitary', 'doubt', 'acid', 'slip', 'speak', 'deceive', 'apparatus', 'flow