# COM4008 Programming Concepts: NumPy, pandas and Data Visualisation

This content is designed as four linked VLE information pages. Lecture 9 demonstrates how earlier programming concepts support an introductory data-analysis workflow.

---

# Page 1: Matrices, Images and NumPy Arrays

## On this page

- Images as numerical arrays
- Pixels, channels and colour values
- Raw image size
- Python lists compared with NumPy arrays
- Data types, shape and dimensions
- Creating, reshaping, indexing and slicing arrays
- Vectorised calculations

## Learning outcomes

By the end of this page, you should be able to:

- explain how a digital image can be represented numerically;
- calculate the number of values in a simple image array;
- create NumPy arrays with a selected data type;
- inspect an array's shape, size and number of dimensions;
- reshape an array when the element count remains compatible;
- select rows, columns and regions from a two-dimensional array;
- perform simple element-wise calculations without an explicit Python loop.

## Why begin with images?

Computer vision is one striking example of numerical computing. A computer does not initially experience an image as “a flower” or “a face”; software receives organised numerical values.

A greyscale image can be represented as a two-dimensional array:

```text
rows × columns
```

In a common unsigned 8-bit representation, each pixel value is from 0 to 255:

- `0` represents black;
- `255` represents white;
- intermediate values represent shades of grey.

Different imaging formats and transformations can use other ranges or conventions, so always check the data being processed.

## Colour channels

An RGB image stores red, green and blue channel values for each pixel. A pixel such as:

```python
[0, 255, 0]
```

represents full green with no red or blue in the common RGB ordering.

A colour image is commonly represented with shape:

```text
height × width × channels
```

For a 1080 × 1920 RGB image:

```python
height = 1080
width = 1920
channels = 3

pixel_count = height * width
value_count = height * width * channels

print(pixel_count)  # 2,073,600 pixels
print(value_count)  # 6,220,800 channel values
```

The image has approximately 2.07 megapixels, not 6.22 megapixels. The larger number counts channel values.

If every channel value uses one byte, the raw pixel data requires 6,220,800 bytes: approximately 6.22 MB using decimal units, or 5.93 MiB using binary units. File headers, metadata and row layout may add overhead.

JPEG—named after the Joint Photographic Experts Group—usually compresses photographic data using lossy compression. Its file size depends on image content and quality settings, so there is no single guaranteed ratio.

## Decimal, binary and hexadecimal colour

One byte contains eight bits and can represent unsigned values from 0 to 255:

```python
print(bin(255))  # 0b11111111
print(hex(255))  # 0xff
```

Web colours often use two hexadecimal digits per RGB channel:

```python
red = 0
green = 255
blue = 0

colour = f"#{red:02x}{green:02x}{blue:02x}"
print(colour)  # #00ff00
```

Formatting with `02x` produces exactly two lowercase hexadecimal digits. Concatenating separate `hex()` results would leave unwanted `0x` prefixes.

## What is NumPy?

NumPy—Numerical Python—is a third-party package providing efficient multidimensional arrays and numerical operations.

```python
import numpy as np
```

NumPy is commonly available in scientific Python environments. In another environment it may need installation. Install packages in the same environment that runs the notebook or script; avoid repeatedly placing installation commands inside normal program code.

## Python lists and NumPy arrays

```python
python_list = [1, 2, 3, 4]
numpy_array = np.array([1, 2, 3, 4])
```

| Feature | Python list | NumPy `ndarray` |
|---|---|---|
| Intended purpose | General collection | Homogeneous numerical array |
| Element representation | References to Python objects | Usually one fixed data type in a compact buffer |
| Dimensions | Nested lists by convention | Explicit multidimensional shape |
| Arithmetic | List-specific behaviour | Element-wise and vectorised operations |
| Resizing | Designed to grow and shrink | Shape is normally fixed; operations create or reshape arrays |

NumPy arrays normally have one `dtype`. NumPy chooses a common representation where possible:

```python
values = np.array([3.14, 2, 3, 4])
print(values)
print(values.dtype)
```

The integers are represented as floating-point values. Mixing numbers and text may produce a string array rather than an error:

```python
mixed = np.array([1, 2.0, True, "Nick"])
print(mixed.dtype)
```

NumPy can also hold Python objects using `dtype=object`, but that loses many memory and speed advantages. “Homogeneous numerical data” is the useful default model, not an absolute claim that arrays can only contain integers.

## Choosing a data type

Specify a data type when precision, range or memory matters:

```python
values = np.array([1, 2, 3], dtype=np.float32)

print(values.dtype)
print(values.itemsize)  # bytes per element
print(values.nbytes)    # bytes in the data buffer
```

`float32` uses four bytes per value. `float64` uses eight. Smaller types save memory but have reduced precision or range.

`nbytes` reports the array data buffer, not necessarily every Python-level object and overhead associated with the array.

## Creating arrays

Useful constructors include:

```python
print(np.arange(0, 11, 2))
print(np.zeros(10))
print(np.ones(7))
print(np.full(10, 8))
```

`np.arange(start, stop, step)` excludes the stop value, like `range()`.

For evenly spaced floating-point samples including a controlled endpoint, `linspace()` is often preferable:

```python
samples = np.linspace(0, 1, 5)
```

## Dimensions, shape and size

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

print(matrix.ndim)   # 2
print(matrix.shape)  # (2, 3)
print(matrix.size)   # 6
```

- `ndim` is the number of axes;
- `shape` gives the length of each axis;
- `size` is the total number of elements.

A colour image may have `ndim == 3` and shape `(height, width, channels)`.

## Reshaping

Reshape without changing the number of elements:

```python
values = np.arange(1, 7)
matrix = values.reshape(2, 3)
```

Six values can form shapes `(2, 3)`, `(3, 2)`, `(1, 6)` or `(6, 1)`, but not `(4, 2)`.

Let NumPy infer one dimension:

```python
matrix = np.arange(1, 13).reshape(3, -1)
```

The result has shape `(3, 4)`.

## Indexing rows and columns

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
```

Select one element using row then column:

```python
print(matrix[1, 2])  # 6
```

Select rows and columns:

```python
print(matrix[0, :])  # first row
print(matrix[:, 0])  # first column
print(matrix[:, 1])  # middle column
```

Select a rectangular region:

```python
print(matrix[0:2, 1:3])
```

Stop indexes are excluded.

## Views and copies

Many basic NumPy slices return a **view** sharing the original data:

```python
values = np.arange(6)
section = values[1:4]
section[0] = 99

print(values)  # original may reflect the change
```

Request an independent copy when needed:

```python
section = values[1:4].copy()
```

This differs from ordinary list slicing, which creates a new outer list.

## Vectorised operations

NumPy applies operations across arrays:

```python
values = np.array([1, 2, 3, 4])

print(values * 10)
print(values ** 2)
print(values.mean())
```

Boolean expressions produce masks:

```python
print(values[values % 2 == 0])
```

This selects even values without writing an explicit Python loop. Vectorisation is central to NumPy's expressive and efficient numerical style.

## A small image-style transformation

Represent a tiny greyscale image:

```python
image = np.array([
    [0, 50, 100],
    [150, 200, 255],
], dtype=np.uint8)
```

Invert it safely:

```python
inverted = 255 - image
```

The array operation applies to every pixel. Real computer-vision workflows also consider colour ordering, clipping, data types, spatial axes and file decoding, but this captures the central idea.

## Pause and predict

Predict the shape and output:

```python
values = np.arange(1, 13).reshape(3, 4)

print(values.shape)
print(values[1, :])
print(values[:, -1])
print(values[values > 8])
```

## Common mistakes

- Reversing black and white in the common 8-bit greyscale convention.
- Confusing channel values with pixels or megapixels.
- Calling bytes “megapixels.”
- Assuming every NumPy array must contain integers.
- Ignoring `dtype` conversion when mixing values.
- Reshaping to an incompatible element count.
- Swapping row and column indexes.
- Assuming a NumPy slice is always an independent copy.
- Using Python loops where a clear vectorised operation exists.

## Check your understanding

1. What does a greyscale pixel value represent?
2. What shape might an RGB image have?
3. How do `shape`, `size` and `ndim` differ?
4. What is a NumPy `dtype`?
5. Why can six values reshape to `(2, 3)` but not `(4, 2)`?
6. How do basic NumPy slices differ from list slices?
7. What is vectorisation?

## Apply your learning

1. Create arrays of ten zeros, seven ones, values 10–50, and odd values 51–99.
2. Reshape values 1–25 into a 5 × 5 matrix and select its middle column.
3. Create a random 3 × 3 integer array using `np.random.default_rng()`.
4. Build a small greyscale matrix and calculate an inverted version.
5. Create a character pyramid first with strings, then optionally represent it in a two-dimensional array.

## Page summary

Images motivate multidimensional numerical arrays: pixels occupy spatial positions and colour adds channels. NumPy arrays provide explicit shape, homogeneous data representation, multidimensional indexing and vectorised operations. Careful attention to data types, units, views and axes is essential for reliable numerical work.

**Next:** Continue to **Page 2: Tabular Data with pandas**.

---

# Page 2: Tabular Data with pandas

## On this page

- Series and DataFrames
- Reading CSV files
- Tidy rows and columns
- Inspecting structure and missing values
- Selecting rows and columns
- Creating and removing columns
- Filtering data
- Descriptive statistics
- Writing data back to CSV

## Learning outcomes

By the end of this page, you should be able to:

- distinguish a pandas Series from a DataFrame;
- read a CSV file with meaningful column names;
- inspect data types, dimensions and missing values;
- select rows and columns using labels and positions;
- create calculated columns;
- filter rows using Boolean conditions;
- calculate introductory descriptive statistics;
- save a cleaned DataFrame.

## Why pandas?

pandas is a third-party library for labelled and tabular data. It builds on NumPy and provides structures suited to datasets in which rows represent observations and columns represent variables.

```python
import pandas as pd
```

A spreadsheet-like display is convenient, but a DataFrame is a programmable data structure—not an Excel worksheet embedded in Python.

## Series

A `Series` is a one-dimensional labelled collection:

```python
marks = pd.Series(
    [70, 75, 80],
    index=["Aisha", "Sam", "Robin"],
    name="mark",
)
```

Its index labels identify values:

```python
print(marks["Sam"])
print(marks.mean())
```

A Series does not inherently mean time-series data. It becomes a time series when its index represents dates or times:

```python
dates = pd.to_datetime(["2025-10-27", "2025-10-28", "2025-10-29"])
activity = pd.Series([70, 75, 80], index=dates)
```

## DataFrames

A `DataFrame` is a two-dimensional labelled table:

```python
students = pd.DataFrame(
    {
        "name": ["Nick", "Sam", "Lucy"],
        "student_id": [12345678, 87654321, 23451311],
        "mark": [67, 78, 54],
    }
)
```

Columns may have different data types. Within one column, a consistent type normally makes analysis easier.

## Reading a CSV

CSV means comma-separated values. A clean file might contain:

```text
name,student_id,mark
Nick,12345678,67
Sam,87654321,78
Lucy,23451311,54
```

Read it with:

```python
students = pd.read_csv("students.csv")
```

The supplied `students.txt` has spaces after delimiters and a trailing comma, which can create padded names and an unwanted empty column. A cleaned CSV is preferable. When reading the existing form:

```python
students = pd.read_csv("students.txt", skipinitialspace=True)
students = students.dropna(axis="columns", how="all")
students.columns = students.columns.str.strip()
```

Fix the source format where possible rather than accumulating cleanup code.

## Local files and URLs

`read_csv()` can read a local path or an accessible raw CSV URL:

```python
students = pd.read_csv("data/students.csv")
```

Remote data introduces network availability and reproducibility concerns. For a taught practical, provide a local course copy with a source citation. This ensures every learner analyses the same snapshot.

## Reading the Iris dataset

The classic Iris dataset contains four measurements and a species label. If the source file has no header, provide names:

```python
column_names = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species",
]

iris = pd.read_csv("iris.csv", names=column_names)
```

This direct pandas route is simpler for tabular teaching than first creating a structured NumPy array and then converting it. NumPy remains the foundation for numerical arrays; pandas provides the labelled table layer.

## Inspect before analysing

Never assume a file loaded correctly merely because no exception occurred:

```python
print(iris.head())
print(iris.tail())
print(iris.shape)
print(iris.columns)
print(iris.dtypes)
iris.info()
```

Check missing values:

```python
print(iris.isna().sum())
```

Inspect unexpected categories:

```python
print(iris["species"].value_counts(dropna=False))
```

Data cleaning is part of analysis, not an optional cosmetic step.

## Selecting columns

One column returns a Series:

```python
petal_width = iris["petal_width"]
```

Several columns return a DataFrame:

```python
petals = iris[["petal_length", "petal_width"]]
```

Attribute syntax such as `iris.petal_width` is less robust when names contain spaces, collide with methods, or are constructed dynamically. Bracket syntax is the reliable default.

## Selecting rows

Use `loc` for labels and Boolean conditions:

```python
print(iris.loc[0])
print(iris.loc[iris["species"] == "Iris-setosa"])
```

Use `iloc` for integer positions:

```python
print(iris.iloc[0])
print(iris.iloc[0:5, 0:2])
```

Remember: `loc` is label-oriented; `iloc` is position-oriented.

## Filtering rows

Boolean comparisons produce a mask:

```python
wide_petals = iris[iris["petal_width"] > 1.5]
```

Combine conditions with `&` and `|`, placing each comparison in parentheses:

```python
selected = iris[
    (iris["petal_width"] > 1.5)
    & (iris["petal_length"] > 4.5)
]
```

Python's scalar `and` and `or` do not perform element-wise Series comparisons.

## Calculated columns

Vectorised expressions create columns:

```python
iris["petal_area_proxy"] = (
    iris["petal_length"] * iris["petal_width"]
)
```

Call this an area proxy rather than a true petal volume: multiplying length by width is a simplified derived measure, and width squared would require a justified geometric model.

Remove a column without mutating the original:

```python
reduced = iris.drop(columns=["petal_area_proxy"])
```

Or replace the variable deliberately:

```python
iris = iris.drop(columns=["petal_area_proxy"])
```

## Descriptive statistics

```python
print(iris["petal_width"].count())
print(iris["petal_width"].min())
print(iris["petal_width"].max())
print(iris["petal_width"].mean())
print(iris["petal_width"].median())
```

Summarise numeric columns:

```python
print(iris.describe())
```

Compare groups:

```python
species_means = iris.groupby("species").mean(numeric_only=True)
print(species_means)
```

Summary statistics describe a dataset; they do not explain causes or establish statistical significance.

## Student-object data to CSV

Convert objects to row dictionaries:

```python
rows = [
    {
        "name": student.name,
        "student_id": student.student_id,
        "mark": student.mark,
    }
    for student in students
]

student_frame = pd.DataFrame(rows)
student_frame.to_csv("students.csv", index=False)
```

This avoids manually concatenating commas and accidentally producing malformed rows.

Read and locate the highest mark:

```python
highest_index = student_frame["mark"].idxmax()
highest_student = student_frame.loc[highest_index]
```

If ties matter, select every row equal to the maximum instead:

```python
highest = student_frame[
    student_frame["mark"] == student_frame["mark"].max()
]
```

## Writing cleaned data

```python
iris.to_csv("iris_clean.csv", index=False)
```

The index is often an internal row label rather than source data, so `index=False` avoids writing an unwanted column. Decide deliberately when an index carries meaning.

## Pause and predict

Predict the returned type for each expression:

```python
iris["petal_width"]
iris[["petal_width"]]
iris.loc[0]
iris.loc[[0]]
iris[iris["petal_width"] > 1.5]
```

Then inspect each with `type()` and explain the difference between Series and DataFrame results.

## Common mistakes

- Assuming every Series is a time series.
- Analysing before inspecting columns, types and missing values.
- Using a webpage URL instead of a raw CSV resource.
- Using `and` or `or` for element-wise pandas filters.
- Confusing `loc` labels with `iloc` positions.
- Treating a calculated proxy as a physically accurate measurement.
- Writing object data by manually constructing malformed CSV text.
- Forgetting `index=False` when exporting.
- Assuming `idxmax()` automatically handles ties as intended.

## Check your understanding

1. How does a Series differ from a DataFrame?
2. Why inspect a dataset before analysis?
3. When should `loc` and `iloc` be used?
4. What does a Boolean mask do?
5. Why are parentheses needed around combined conditions?
6. What does `groupby()` help compare?
7. Why is a local teaching copy of remote data useful?

## Apply your learning

1. Clean and load the supplied student data, then identify all highest-mark rows.
2. Save student objects to a well-formed CSV through a DataFrame.
3. Load the Iris data with clear column names and inspect its quality.
4. Calculate summary statistics overall and by species.
5. Create and justify one derived column.
6. Filter the dataset using two numerical conditions.

## Page summary

pandas adds labelled Series and DataFrames to the numerical Python ecosystem. A responsible workflow loads data, inspects structure and quality, selects and filters deliberately, calculates defensible derived values, summarises distributions and groups, and exports clean results. DataFrames are analytical structures rather than merely attractive tables.

**Previous:** Page 1: Matrices, Images and NumPy Arrays  
**Next:** Continue to **Page 3: Exploratory Data Analysis and Visualisation**.

---

# Page 3: Exploratory Data Analysis and Visualisation

## On this page

- The purpose of exploratory data analysis
- Questions before charts
- Matplotlib and Seaborn
- Distribution, relationship and group-comparison plots
- Labels, scales and accessibility
- Interpreting the Iris dataset
- Avoiding misleading visualisations

## Learning outcomes

By the end of this page, you should be able to:

- explain the purpose and limits of exploratory data analysis;
- select a chart appropriate to a simple analytical question;
- create plots with Matplotlib and Seaborn;
- distinguish distributions, relationships and group comparisons;
- label a chart clearly and choose an appropriate scale;
- describe visible patterns without claiming unsupported causation;
- identify common sources of misleading or inaccessible plots.

## What is exploratory data analysis?

**Exploratory data analysis**, or EDA, uses summaries and visualisations to understand a dataset before formal modelling or conclusions.

Typical questions include:

- What values and categories are present?
- Are values missing or implausible?
- How is one variable distributed?
- Do two variables appear related?
- Do groups show different distributions?
- Are there possible outliers?

EDA helps generate questions and detect data-quality issues. It does not by itself prove causes, guarantee predictions, or replace statistical reasoning.

## Begin with a question

Do not begin by calling every available plotting function. Choose a plot based on the question and variable types:

| Question | Possible plot |
|---|---|
| How is one numeric variable distributed? | Histogram, box plot |
| How do two numeric variables relate? | Scatter plot |
| How does a numeric variable differ by category? | Box plot, violin plot |
| How does a value change over ordered time? | Line plot |
| How many observations belong to each category? | Count plot or bar chart |
| How do several numerical variables relate? | Pair plot, used selectively |

The plot is evidence in response to a question, not decoration.

## Matplotlib and Seaborn

Matplotlib provides foundational plotting tools:

```python
import matplotlib.pyplot as plt
```

Seaborn provides statistical plotting functions and works naturally with pandas:

```python
import seaborn as sns
```

Seaborn uses Matplotlib underneath, so Matplotlib controls such as titles, labels, figure size and saving remain useful.

Set a readable theme:

```python
sns.set_theme(style="whitegrid")
```

## A histogram

Explore one numerical distribution:

```python
fig, ax = plt.subplots(figsize=(7, 4))
sns.histplot(data=iris, x="petal_length", bins=15, ax=ax)
ax.set_title("Distribution of petal length")
ax.set_xlabel("Petal length (cm)")
ax.set_ylabel("Number of flowers")
plt.tight_layout()
plt.show()
```

Bin width changes the visible pattern. Try reasonable alternatives rather than treating one histogram as uniquely correct.

## A scatter plot

Explore the relationship between two numerical variables:

```python
fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(
    data=iris,
    x="petal_length",
    y="petal_width",
    hue="species",
    ax=ax,
)
ax.set_title("Petal dimensions by Iris species")
ax.set_xlabel("Petal length (cm)")
ax.set_ylabel("Petal width (cm)")
plt.tight_layout()
plt.show()
```

The plot may show clusters and a positive association. Describe what is visible without claiming that one measurement causes the other.

## A box plot

Compare a numerical distribution across groups:

```python
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(
    data=iris,
    x="species",
    y="petal_length",
    ax=ax,
)
ax.set_title("Petal length by Iris species")
ax.set_xlabel("Species")
ax.set_ylabel("Petal length (cm)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()
```

A box plot summarises median, quartiles and values beyond the whisker rule. Points outside whiskers are possible outliers, not automatically mistakes that should be deleted.

Passing an entire mixed DataFrame to `sns.boxplot(iris)` is less clear than explicitly naming the variables and analytical question.

## Pair plots

A pair plot displays pairwise relationships among several numeric columns:

```python
sns.pairplot(
    iris,
    vars=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    hue="species",
)
plt.show()
```

It provides a broad overview but becomes expensive and visually dense as the number of variables grows. Use a small, purposeful subset and follow up with focused plots.

## Time-series plots

When order represents time, use a line plot:

```python
activity = pd.Series(
    [70, 75, 80, 72, 68],
    index=pd.to_datetime([
        "2025-10-27",
        "2025-10-28",
        "2025-10-29",
        "2025-10-30",
        "2025-10-31",
    ]),
)

activity.plot(marker="o")
plt.title("Activity over time")
plt.xlabel("Date")
plt.ylabel("Activity")
plt.tight_layout()
plt.show()
```

Connecting points implies an ordered progression, so line charts are inappropriate for unordered categories.

## Make plots understandable

A useful plot normally includes:

- a descriptive title;
- axis labels and units;
- a legend when visual encodings need explanation;
- readable category labels;
- appropriate scales and limits;
- enough contrast and size for the viewing context.

Colour should not be the only way to distinguish important categories. Use marker shape, line style, labels, faceting or direct annotation where possible. Consider viewers with colour-vision differences and test plots at the size used in Blackboard.

## Avoid misleading choices

Potential problems include:

- truncating an axis to exaggerate a difference;
- using area or 3D effects that distort comparison;
- showing too many categories or points without managing overlap;
- omitting units or sample size;
- connecting unordered categories with lines;
- choosing colours that imply an unintended ranking;
- reporting only the plot that supports a preferred story;
- treating correlation or visual separation as causation.

For bar charts, a zero baseline is usually important because bar length encodes magnitude. Scatter and line plots may reasonably use focused axes, but disclose scales clearly.

## Separate preparation from plotting

Make the data transformation explicit:

```python
species_summary = (
    iris.groupby("species", as_index=False)["petal_length"]
    .mean()
)
```

Then plot the summary:

```python
sns.barplot(
    data=species_summary,
    x="species",
    y="petal_length",
)
```

This separation makes it easier to verify what each plotted value represents.

Be careful with Seaborn estimators: some functions calculate summaries and uncertainty automatically. Know whether the marks show raw observations, counts, means, medians or model estimates.

## Save a figure

```python
fig.savefig(
    "petal_dimensions.png",
    dpi=200,
    bbox_inches="tight",
)
```

Use informative filenames and retain the code and data snapshot that generated the chart. Reproducibility matters more than manually editing a plot after export.

## Interpret, do not merely produce

A suitable observation might be:

> In this dataset, Iris setosa observations form a visibly separate cluster at lower petal lengths and widths, while the other two species overlap more.

This is bounded by the available dataset and variables. A stronger unsupported claim would be:

> Petal length causes the species.

Species is not caused by the measured petal length; the measurements are characteristics associated with labelled species.

For every plot, write:

1. the question;
2. what each visual channel represents;
3. one visible pattern;
4. one limitation or follow-up question.

## Pause and choose

Choose a plot for each question and justify it:

1. What is the distribution of student marks?
2. Are petal length and width associated?
3. How do petal lengths vary among species?
4. How does activity change over five dates?
5. How many records belong to each category?

## Common mistakes

- Producing plots without an analytical question.
- Using a line chart for unordered categories.
- Omitting labels, units or legends.
- Interpreting every point beyond a box-plot whisker as invalid.
- Treating visual association as causation.
- Creating a pair plot with too many columns.
- Using colour as the only important distinction.
- Failing to inspect the data used by the plotting function.
- Not recording the transformation used to produce aggregated values.

## Check your understanding

1. What is EDA intended to achieve?
2. Which plot suits two numeric variables?
3. What does a box plot summarise?
4. Why can a pair plot become unwieldy?
5. When is a line chart appropriate?
6. Why should preparation and plotting be separated?
7. What is the difference between association and causation?

## Apply your learning

1. Produce a histogram, scatter plot and grouped box plot from Iris.
2. Add meaningful titles, axis labels and units.
3. Write one supported observation and one limitation for each plot.
4. Create a species summary table and plot a selected statistic.
5. Save one publication-ready figure and include alternative text suitable for Blackboard.
6. Find one way a plotting choice could mislead, then correct it.

## Page summary

EDA combines inspection, descriptive statistics and purposeful visualisation. Chart choice should follow a question and the types of variables involved. Matplotlib and Seaborn support distributions, relationships, group comparisons and time trends, but clear labels, accessible encodings and cautious interpretation are essential. A graph suggests patterns; it does not automatically establish causes.

**Previous:** Page 2: Tabular Data with pandas  
**Next:** Continue optionally to **Page 4: API Data to DataFrame**.

---

# Page 4: Optional Application—API Data to DataFrame

## On this page

- The end-to-end data pipeline
- Calling an API safely
- JSON dictionaries and lists
- Normalising records into a DataFrame
- Selecting and cleaning columns
- Missing data and numeric conversion
- Analysing and visualising API results
- Reproducibility and limitations

## Learning outcomes

By the end of this optional page, you should be able to:

- describe a small acquire–inspect–transform–analyse pipeline;
- call an HTTP API with a timeout and status check;
- inspect nested JSON before constructing a DataFrame;
- normalise a list of record dictionaries;
- select available columns safely;
- account for missing values in calculations;
- explain why live API results are less reproducible than a fixed dataset.

## Why this is optional

The API example combines many earlier topics:

- imports and third-party packages;
- functions and parameters;
- exceptions and network failures;
- dictionaries, lists and JSON;
- pandas DataFrames;
- descriptive statistics and plotting.

That makes it an excellent capstone, but a poor place to introduce core pandas concepts for the first time. Complete Pages 1–3 using a stable local dataset before attempting this live-data extension.

## A data pipeline

The example follows this sequence:

```text
Acquire → Validate → Inspect → Normalise → Clean → Analyse → Communicate
```

Each arrow can fail or change the meaning of the data. Keeping stages visible makes debugging and evaluation easier.

## Retrieve JSON safely

The supplied `search_itunes.py` is a useful starting module. Strengthen it with a timeout and allow Requests to raise HTTP errors:

```python
import requests


def search_itunes(query, media_type="music", limit=10):
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be non-empty text")

    response = requests.get(
        "https://itunes.apple.com/search",
        params={
            "term": query.strip(),
            "media": media_type,
            "limit": limit,
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()
```

Network access can fail through timeouts, connection problems, HTTP errors or invalid responses. Catch these at the application boundary where a useful message or retry can be offered.

The external service, parameters and returned fields may change. Check its current documentation before relying on the example in a live session.

## Inspect the returned structure

The top-level response is usually a dictionary containing a count and a list of result dictionaries:

```python
data = search_itunes("Python Programming", "ebook")

print(type(data))
print(data.keys())
print(data.get("resultCount"))
print(type(data.get("results")))
```

Inspect one record before selecting columns:

```python
records = data.get("results", [])

if records:
    print(records[0].keys())
```

Do not begin with:

```python
pd.DataFrame(data)
```

The top-level values have incompatible structures: a scalar count and a list of records. The analytical table lives inside `data["results"]`.

## Create the DataFrame

For a flat list of dictionaries:

```python
frame = pd.DataFrame(records)
```

For nested record fields:

```python
frame = pd.json_normalize(records)
```

The function name uses American spelling: `json_normalize`, not `json_normalise`.

`json_normalize()` flattens nested dictionary paths into columns where possible. Lists nested inside records may still need separate handling.

## Select columns safely

API records may not all contain the same fields. Select the intersection of desired and available columns:

```python
desired_columns = [
    "trackName",
    "artistName",
    "releaseDate",
    "price",
    "averageUserRating",
    "userRatingCount",
]

available_columns = [
    column for column in desired_columns
    if column in frame.columns
]

reduced = frame[available_columns].copy()
```

This prevents a `KeyError`, but it should not silently hide a required field. Decide which columns are optional and which are essential for the question.

## Clean types and missing values

Convert numeric fields:

```python
for column in ["price", "averageUserRating", "userRatingCount"]:
    if column in reduced:
        reduced[column] = pd.to_numeric(
            reduced[column],
            errors="coerce",
        )
```

Invalid or absent values become `NaN`. Inspect them:

```python
print(reduced.isna().sum())
```

Parse dates:

```python
if "releaseDate" in reduced:
    reduced["releaseDate"] = pd.to_datetime(
        reduced["releaseDate"],
        errors="coerce",
        utc=True,
    )
```

Do not replace missing ratings with zero unless zero genuinely means “rated zero.” Missing and zero carry different meanings.

## Analyse with context

```python
if "averageUserRating" in reduced:
    print(reduced["averageUserRating"].describe())
```

Filtering high ratings alone can be misleading when based on very few reviews. Include rating count:

```python
popular_high_rated = reduced[
    (reduced["averageUserRating"] >= 4.0)
    & (reduced["userRatingCount"] >= 10)
]
```

The threshold is an analytical choice that should be explained, not presented as an objective definition of quality.

For track duration, inspect and convert the expected millisecond field:

```python
if "trackTimeMillis" in frame:
    frame["track_minutes"] = (
        pd.to_numeric(frame["trackTimeMillis"], errors="coerce")
        / 60_000
    )
    longest_index = frame["track_minutes"].idxmax()
    print(frame.loc[longest_index])
```

Check that the DataFrame is non-empty and the converted column contains values before calling `idxmax()`.

## Visualise one defensible question

For example: among returned items with both values present, is rating related to rating count?

```python
plot_data = reduced.dropna(
    subset=["averageUserRating", "userRatingCount"]
)

sns.scatterplot(
    data=plot_data,
    x="userRatingCount",
    y="averageUserRating",
)
plt.xscale("log")
plt.title("Ratings among returned search results")
plt.xlabel("User rating count (log scale)")
plt.ylabel("Average user rating")
plt.tight_layout()
plt.show()
```

The chart describes only this API response for this query and time. It is not a representative study of all media or users.

## Cache a reproducible snapshot

Live results can change. Save the raw response with metadata:

```python
import json
from datetime import datetime, timezone

snapshot = {
    "retrieved_at": datetime.now(timezone.utc).isoformat(),
    "query": "Python Programming",
    "media_type": "ebook",
    "response": data,
}

with open("itunes_snapshot.json", "w", encoding="utf-8") as file:
    json.dump(snapshot, file, indent=2)
```

Analyse the stored snapshot in a taught practical. This separates acquisition from analysis and preserves what learners actually used.

Do not redistribute data without considering service terms, personal data, licensing and institutional requirements.

## Exception handling at the boundary

```python
import requests


def main():
    try:
        data = search_itunes("Python Programming", "ebook")
    except ValueError as error:
        print(f"Invalid search: {error}")
        return 1
    except requests.RequestException as error:
        print(f"The service could not be reached: {error}")
        return 1

    records = data.get("results", [])
    if not records:
        print("No results were returned.")
        return 0

    frame = pd.json_normalize(records)
    print(frame.head())
    return 0
```

The acquisition function raises; the entry point communicates with the user.

## Pause and diagnose

Explain what is wrong with each approach:

```python
frame = pd.DataFrame(search_itunes("Python", "ebook"))
```

```python
reduced = frame[["averageUserRating", "price"]]
```

```python
frame["averageUserRating"] = frame["averageUserRating"].fillna(0)
```

```python
response = requests.get(url)
```

Suggest a safer alternative for each.

## Common mistakes

- Making live API retrieval a prerequisite for learning core pandas operations.
- Constructing a DataFrame from the wrong level of nested JSON.
- Misspelling `json_normalize()`.
- Assuming every result has every field.
- Omitting a network timeout.
- Treating missing ratings as zero.
- Filtering by average rating without considering rating count.
- Claiming live search results represent a population.
- Failing to preserve the query, retrieval time and raw response.
- Allowing an external service change to break the entire taught session.

## Check your understanding

1. Why is the API activity optional?
2. What does `response.raise_for_status()` do?
3. Which part of the response becomes the row records?
4. When is `pd.json_normalize()` useful?
5. Why should optional and required columns be distinguished?
6. Why is missing data different from zero?
7. How does saving a snapshot improve reproducibility?

## Apply your learning

1. Import `search_itunes()` from its module and retrieve a small result set safely.
2. Inspect the response structure and normalise only the record list.
3. Select available analytical columns and report missing values.
4. Answer one question using a table and one purposeful plot.
5. Save the raw response and retrieval metadata as JSON.
6. Re-run the analysis from the stored snapshot without network access.

## Page summary

An API-to-DataFrame workflow combines acquisition, validation, nested JSON inspection, normalisation, cleaning, analysis and communication. Live data adds failure modes and reproducibility problems, so a stable local dataset should teach the core concepts first. Optional API work then demonstrates how earlier Python skills combine in an authentic pipeline.

**Previous:** Page 3: Exploratory Data Analysis and Visualisation  
**Next step:** Complete the Lecture 9 data investigation and document the question, source, preparation, findings and limitations.

---

# Suggested VLE setup

Create one learning module titled **9 Python for Data Analysis**, containing:

1. **Start here: from Python programs to data workflows**
2. **9.1 Matrices, Images and NumPy Arrays**
3. **9.2 Tabular Data with pandas**
4. **9.3 Exploratory Data Analysis and Visualisation**
5. **9.4 Optional: API Data to DataFrame**
6. **Data investigation practical**
7. **Check your learning**

Do not create a separate 9.0 page. Computer vision is the motivating context at the beginning of 9.1, allowing image matrices to lead directly into NumPy shape, data types, indexing and vectorisation.

The core practical should use supplied local copies of `students.csv` and the Iris dataset. Keep the API work optional and provide a stored JSON snapshot so network availability cannot block learning. The Mario pyramid is useful iteration practice but is peripheral to the data-science narrative; retain it as an optional NumPy-grid challenge rather than a core destination.
