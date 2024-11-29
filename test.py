from dataset import Dataset
import pandas as pd

df = pd.DataFrame({

})

ds = Dataset(df)

ds.preparing(clear_type="z", strategy="Onehot")

ds.display()

ds.prepare_for_cross_validation(n_splits=2, stratify_by="area")

ds.transform(library="torch")
