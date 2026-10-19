from emotion_detection import emotion_detector

result = emotion_detector('I am really mad about this')
assert 'emotionPredictions' in result
print('Test passed: emotion_detector returned a response')
