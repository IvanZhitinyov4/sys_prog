from dataset import Dataset
import pandas as pd

# взял датафрейм у Головко Вадима.
df = pd.DataFrame({
    "form": ['circle', 'rectangle', 'square', None, 'circle', 'rectangle', 'square', 'rhombus', 'circle'],
    "color": ['red', 'purple', None, 'violet', 'purple', 'white', 'black', 'yellow', 'purple'],
    "area": [10, 10, 15, 24, 39, 9, 1000000, 23, 1000],
    "priority": [3, 1, 2, 4, None, 1, 2, 4, 5],
})

ds = Dataset(df)

ds.preparing(strategy="mean", encoding_type='Onehot')

ds.display()

print(ds.prepare_for_cross_validation(n_splits=2, stratify_by="area"))

ds.transform(library="tensorflow")
