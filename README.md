# attentionviz
Creating word-weighted heatmap's latex script given a list of tokens and attention scores
## How to use
```python3
from heatmap import Visualizer
viz = Visualizer()

word_list = [['This', 'script', 'generates', 'heatmaps'], ['Change', 'this', 'to', 'try', 'the', 'visualizer']]
attention_list = [[0, 70, 0, 80], [0, 50, 0, 0, 0, 70]]
label_list = ['Description', 'Experiment']

viz.visualize(word_list, attention_list, label_list,
              latex_file='sample.tex',
              title='Generating heatmaps',
              batch_size=len(word_list),
              color='blue')
# Copy the content of sample.tex on overleaf and compile to view the heatmap
```
