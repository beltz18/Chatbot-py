# Chatbot Project

This Chatbot uses deep learning to transform a word sequence into a response.
Needs a .json file that loads the necesary data with intents > tags, patterns and responses

## .json file

The .json file must be called data-bot and should have the next data structure:

{
  "intents": [
  {
    "tag": "tag1",
    "patterns":
    [
      "pattern1",
      "pattern2",
      "pattern3"
    ],
    "responses":
    [
      "response1",
      "response2",
      "response3"
    ]
  },
  {
    ...
  }
}

### feedback

Some things can improve and optimize, you are authorized to do so :)