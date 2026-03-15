{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b2933cd1-c9db-42f5-bb8f-1c3a4baa61db",
   "metadata": {},
   "source": [
    "## Women Safety Analytics & Safety Score Calculation\n",
    "### This notebook performs Exploratory Data Analysis (EDA) and builds a safety scoring mechanism based on crime data. Key Steps:\n",
    "\n",
    "### Data Filtering: Focusing specifically on female victims.\n",
    "### Feature Engineering: Extracting temporal features (Hour, Month) and encoding locations.\n",
    "### Clustering: Using K-Means to identify high-risk crime clusters.\n",
    "### Anomaly Detection: Using Isolation Forest to find unusual crime patterns.\n",
    "### Safety Scoring: Calculating a heuristic safety score (0-100) for various locations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93b7dc2d-fdd0-4af1-8c78-6aa41f7e4689",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "fb700b19-2313-452b-a78d-d7a76bdcf5e8",
   "metadata": {},
   "source": [
    "## 1. Environment Setup & Library Imports\n",
    "### Importing all necessary libraries for data manipulation, machine learning, and system operations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "43bc7e3a-0671-44e5-8563-5610f4b30263",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os\n",
    "import joblib\n",
    "\n",
    "# Scikit-learn imports for preprocessing and modeling\n",
    "from sklearn.preprocessing import LabelEncoder, StandardScaler\n",
    "from sklearn.cluster import KMeans\n",
    "from sklearn.ensemble import IsolationForest\n",
    "\n",
    "# Setup directories for outputs\n",
    "os.makedirs('../data', exist_ok=True)\n",
    "os.makedirs('../models', exist_ok=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1145742-4ec4-4d8e-b163-c1fbad683e1b",
   "metadata": {},
   "source": [
    "## 2. Data Loading & Initial Filtering\n",
    "### We load the raw crime dataset and filter it to focus exclusively on crimes committed against women."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1c0f1678-66c2-4d10-a894-23d0467fabb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Dataset Shape: (40160, 14)\n",
      "Women Safety Dataset Shape: (22423, 14)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Report Number</th>\n",
       "      <th>Date Reported</th>\n",
       "      <th>Date of Occurrence</th>\n",
       "      <th>Time of Occurrence</th>\n",
       "      <th>City</th>\n",
       "      <th>Crime Code</th>\n",
       "      <th>Crime Description</th>\n",
       "      <th>Victim Age</th>\n",
       "      <th>Victim Gender</th>\n",
       "      <th>Weapon Used</th>\n",
       "      <th>Crime Domain</th>\n",
       "      <th>Police Deployed</th>\n",
       "      <th>Case Closed</th>\n",
       "      <th>Date Case Closed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>02-01-2020 05:00</td>\n",
       "      <td>01-01-2020 02:00</td>\n",
       "      <td>01-01-2020 14:30</td>\n",
       "      <td>Ludhiana</td>\n",
       "      <td>271</td>\n",
       "      <td>KIDNAPPING</td>\n",
       "      <td>48</td>\n",
       "      <td>F</td>\n",
       "      <td>Blunt Object</td>\n",
       "      <td>Other Crime</td>\n",
       "      <td>15</td>\n",
       "      <td>No</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>01-01-2020 05:00</td>\n",
       "      <td>01-01-2020 03:00</td>\n",
       "      <td>01-01-2020 14:46</td>\n",
       "      <td>Pune</td>\n",
       "      <td>170</td>\n",
       "      <td>BURGLARY</td>\n",
       "      <td>49</td>\n",
       "      <td>F</td>\n",
       "      <td>Firearm</td>\n",
       "      <td>Other Crime</td>\n",
       "      <td>1</td>\n",
       "      <td>Yes</td>\n",
       "      <td>29-04-2020 05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>01-01-2020 21:00</td>\n",
       "      <td>01-01-2020 04:00</td>\n",
       "      <td>01-01-2020 16:51</td>\n",
       "      <td>Pune</td>\n",
       "      <td>421</td>\n",
       "      <td>VANDALISM</td>\n",
       "      <td>30</td>\n",
       "      <td>F</td>\n",
       "      <td>Other</td>\n",
       "      <td>Other Crime</td>\n",
       "      <td>18</td>\n",
       "      <td>Yes</td>\n",
       "      <td>08-01-2020 21:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>01-01-2020 16:00</td>\n",
       "      <td>01-01-2020 06:00</td>\n",
       "      <td>01-01-2020 14:08</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>172</td>\n",
       "      <td>VEHICLE - STOLEN</td>\n",
       "      <td>64</td>\n",
       "      <td>F</td>\n",
       "      <td>Knife</td>\n",
       "      <td>Violent Crime</td>\n",
       "      <td>13</td>\n",
       "      <td>Yes</td>\n",
       "      <td>24-03-2020 16:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>13</td>\n",
       "      <td>01-01-2020 16:00</td>\n",
       "      <td>01-01-2020 12:00</td>\n",
       "      <td>01-01-2020 23:14</td>\n",
       "      <td>Visakhapatnam</td>\n",
       "      <td>498</td>\n",
       "      <td>FRAUD</td>\n",
       "      <td>36</td>\n",
       "      <td>F</td>\n",
       "      <td>Poison</td>\n",
       "      <td>Other Crime</td>\n",
       "      <td>3</td>\n",
       "      <td>Yes</td>\n",
       "      <td>29-02-2020 16:00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Report Number     Date Reported Date of Occurrence Time of Occurrence  \\\n",
       "2               3  02-01-2020 05:00   01-01-2020 02:00   01-01-2020 14:30   \n",
       "3               4  01-01-2020 05:00   01-01-2020 03:00   01-01-2020 14:46   \n",
       "4               5  01-01-2020 21:00   01-01-2020 04:00   01-01-2020 16:51   \n",
       "6               7  01-01-2020 16:00   01-01-2020 06:00   01-01-2020 14:08   \n",
       "12             13  01-01-2020 16:00   01-01-2020 12:00   01-01-2020 23:14   \n",
       "\n",
       "             City  Crime Code Crime Description  Victim Age Victim Gender  \\\n",
       "2        Ludhiana         271        KIDNAPPING          48             F   \n",
       "3            Pune         170          BURGLARY          49             F   \n",
       "4            Pune         421         VANDALISM          30             F   \n",
       "6         Chennai         172  VEHICLE - STOLEN          64             F   \n",
       "12  Visakhapatnam         498             FRAUD          36             F   \n",
       "\n",
       "     Weapon Used   Crime Domain  Police Deployed Case Closed  Date Case Closed  \n",
       "2   Blunt Object    Other Crime               15          No               NaN  \n",
       "3        Firearm    Other Crime                1         Yes  29-04-2020 05:00  \n",
       "4          Other    Other Crime               18         Yes  08-01-2020 21:00  \n",
       "6          Knife  Violent Crime               13         Yes  24-03-2020 16:00  \n",
       "12        Poison    Other Crime                3         Yes  29-02-2020 16:00  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Load the dataset\n",
    "df = pd.read_csv(\"../Indian Crimes Dataset/crime_dataset_india.csv\")\n",
    "\n",
    "# Filter for Female victims only\n",
    "df_women = df[df['Victim Gender'] == 'F'].copy()\n",
    "\n",
    "print(f\"Original Dataset Shape: {df.shape}\")\n",
    "print(f\"Women Safety Dataset Shape: {df_women.shape}\")\n",
    "df_women.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee67f3ef-7ac6-49a1-aa24-9e6da21d05af",
   "metadata": {},
   "source": [
    "## columns "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1451802d-093a-42fb-bcce-5e2b1a1aac00",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Report Number', 'Date Reported', 'Date of Occurrence',\n",
       "       'Time of Occurrence', 'City', 'Crime Code', 'Crime Description',\n",
       "       'Victim Age', 'Victim Gender', 'Weapon Used', 'Crime Domain',\n",
       "       'Police Deployed', 'Case Closed', 'Date Case Closed'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b0d998d9-1361-40ba-a085-aa3a7887f024",
   "metadata": {},
   "source": [
    "## 5. Date & Time Preprocessing \n",
    "### Convert date columns to datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d7d43c63-4f17-4c73-b83e-96c0b2ff064d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_women['Date of Occurrence'] = pd.to_datetime(\n",
    "    df_women['Date of Occurrence'], errors='coerce'\n",
    ")\n",
    "\n",
    "df_women['Date Reported'] = pd.to_datetime(\n",
    "    df_women['Date Reported'], errors='coerce'\n",
    ")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2c1b8c21-4c08-406e-b2d3-12d991338364",
   "metadata": {},
   "source": [
    "## Convert Time of Occurrence correctly and extract hour\n",
    "\n",
    "### Time column contains full datetime → DO NOT use %H:%M"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "74f85dde-2641-4f7b-8e6f-dc3ef49dbb85",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_women['Time of Occurrence'] = pd.to_datetime(\n",
    "    df_women['Time of Occurrence'], errors='coerce'\n",
    ")\n",
    "\n",
    "df_women['hour'] = df_women['Time of Occurrence'].dt.hour\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26e9f90f-cd5e-45dd-9b85-3da112dae80f",
   "metadata": {},
   "source": [
    "## Handle missing hour values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8d8f965a-573c-4e46-896c-24a5dd5611c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Missing hour values: 0\n"
     ]
    }
   ],
   "source": [
    "median_hour = df_women['hour'].median()\n",
    "df_women['hour'] = df_women['hour'].fillna(median_hour)\n",
    "\n",
    "print(\"Missing hour values:\", df_women['hour'].isna().sum())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e538cb62-e2a3-4736-947e-1723437c7516",
   "metadata": {},
   "source": [
    "## Extract additional temporal features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fc502ab1-9be8-4c87-8046-b60a47ee8429",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_women['month'] = df_women['Date of Occurrence'].dt.month\n",
    "df_women['dayofweek'] = df_women['Date of Occurrence'].dt.dayofweek\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb3991e5-fe6e-48aa-b5a6-1e5152209362",
   "metadata": {},
   "source": [
    "## Verify preprocessing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ccc18aee-778b-4703-9b9a-318a58458766",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Time of Occurrence</th>\n",
       "      <th>hour</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2020-01-01 14:30:00</td>\n",
       "      <td>14.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2020-01-01 14:46:00</td>\n",
       "      <td>14.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2020-01-01 16:51:00</td>\n",
       "      <td>16.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2020-01-01 14:08:00</td>\n",
       "      <td>14.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>2020-01-01 23:14:00</td>\n",
       "      <td>23.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>2020-01-01 22:28:00</td>\n",
       "      <td>22.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>2020-01-01 18:54:00</td>\n",
       "      <td>18.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>2020-01-01 23:09:00</td>\n",
       "      <td>23.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>2020-02-01 18:02:00</td>\n",
       "      <td>18.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>2020-02-01 02:33:00</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Time of Occurrence  hour\n",
       "2  2020-01-01 14:30:00  14.0\n",
       "3  2020-01-01 14:46:00  14.0\n",
       "4  2020-01-01 16:51:00  16.0\n",
       "6  2020-01-01 14:08:00  14.0\n",
       "12 2020-01-01 23:14:00  23.0\n",
       "14 2020-01-01 22:28:00  22.0\n",
       "15 2020-01-01 18:54:00  18.0\n",
       "17 2020-01-01 23:09:00  23.0\n",
       "19 2020-02-01 18:02:00  18.0\n",
       "20 2020-02-01 02:33:00   2.0"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women[['Time of Occurrence', 'hour']].head(10)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b50f4798-6cb0-4d6d-90dc-e4aae4653670",
   "metadata": {},
   "source": [
    "## 6. Encode City Feature"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8164ee38-05ca-4a4d-ab99-51d386e9dfc9",
   "metadata": {},
   "outputs": [],
   "source": [
    "le_city = LabelEncoder()\n",
    "df_women['city_encoded'] = le_city.fit_transform(df_women['City'])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c53abe9e-b021-4382-9809-67c667609d2d",
   "metadata": {},
   "source": [
    "## 7. Select Features for ML Models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8e4be62f-8c30-4473-bb15-4c4ff1659f31",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hour</th>\n",
       "      <th>Victim Age</th>\n",
       "      <th>month</th>\n",
       "      <th>dayofweek</th>\n",
       "      <th>city_encoded</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>14.0</td>\n",
       "      <td>48</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>14.0</td>\n",
       "      <td>49</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>16.0</td>\n",
       "      <td>30</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>14.0</td>\n",
       "      <td>64</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>23.0</td>\n",
       "      <td>36</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    hour  Victim Age  month  dayofweek  city_encoded\n",
       "2   14.0          48      1          2            15\n",
       "3   14.0          49      1          2            21\n",
       "4   16.0          30      1          2            21\n",
       "6   14.0          64      1          2             4\n",
       "12  23.0          36      1          2            28"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "features = [\n",
    "    'hour',\n",
    "    'Victim Age',\n",
    "    'month',\n",
    "    'dayofweek',\n",
    "    'city_encoded'\n",
    "]\n",
    "\n",
    "X = df_women[features].copy()\n",
    "X.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd4dc117-7e73-4a5b-8faa-a7a44d8be5b6",
   "metadata": {},
   "source": [
    "## 8. Feature Scaling"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e91d9e88-e041-4fce-98e1-41cdc48019a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "scaler = StandardScaler()\n",
    "X_scaled = scaler.fit_transform(X)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be9f099d-d24d-4064-bedf-1b01920e65e4",
   "metadata": {},
   "source": [
    "## 9. Clustering Unsafe Patterns (KMeans)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "96efdf99-2d04-4c34-9ba5-114665287a06",
   "metadata": {},
   "outputs": [],
   "source": [
    "kmeans = KMeans(n_clusters=4, random_state=42)\n",
    "df_women['cluster'] = kmeans.fit_predict(X_scaled)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7c1f8e46-45bf-4f9d-8120-60411abc307b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cluster\n",
       "3    6758\n",
       "2    6565\n",
       "1    6496\n",
       "0    2604\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women['cluster'].value_counts()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bd1491a6-13a8-4da5-975f-26a2cbdfa18c",
   "metadata": {},
   "source": [
    "## Cluster Interpretation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "4b683c20-8270-4e0f-aa39-08662eadb8c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hour</th>\n",
       "      <th>Victim Age</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cluster</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3.054147</td>\n",
       "      <td>43.954685</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>12.198584</td>\n",
       "      <td>44.980296</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>12.213861</td>\n",
       "      <td>44.390861</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>12.260580</td>\n",
       "      <td>43.586268</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              hour  Victim Age\n",
       "cluster                       \n",
       "0         3.054147   43.954685\n",
       "1        12.198584   44.980296\n",
       "2        12.213861   44.390861\n",
       "3        12.260580   43.586268"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women.groupby('cluster')[['hour', 'Victim Age']].mean()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c278dbd5-72c1-4f42-b730-e0726e41c472",
   "metadata": {},
   "source": [
    "## 10. Detect Unusual / High-Risk Incidents (Isolation Forest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8fbd5621-bfac-4b15-b518-3a19efa1e4ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "iso = IsolationForest(\n",
    "    contamination=0.1,  # 10% unusual cases\n",
    "    random_state=42\n",
    ")\n",
    "\n",
    "df_women['anomaly'] = iso.fit_predict(X_scaled)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "0e1f73ee-97bf-4a3c-87b1-6762ba463bbf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "anomaly\n",
       " 1    20180\n",
       "-1     2243\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women['anomaly'].value_counts()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e82c610c-d08c-4cc1-b7a2-bb986fa58612",
   "metadata": {},
   "source": [
    "## Build Women Safety Score (0–100)\n",
    "### Logic:\n",
    "### Night crimes → lower score\n",
    "### Anomalies → lower score\n",
    "### Higher clusters → lower score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1877d12f-5168-49a1-a2c6-7086bd9ba9c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_women['safety_score'] = 100\n",
    "\n",
    "# Night time penalty\n",
    "df_women.loc[(df_women['hour'] >= 20) | (df_women['hour'] <= 5), 'safety_score'] -= 20\n",
    "\n",
    "# Anomaly penalty\n",
    "df_women.loc[df_women['anomaly'] == -1, 'safety_score'] -= 30\n",
    "\n",
    "# Cluster penalty\n",
    "df_women['safety_score'] -= df_women['cluster'] * 5\n",
    "\n",
    "# Clip scores\n",
    "df_women['safety_score'] = df_women['safety_score'].clip(0, 100)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6a37243-6a75-48c9-a7f6-807aecbde196",
   "metadata": {},
   "source": [
    "### Safety Score Distribution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "a7d82ca5-06ab-486a-89f5-14e2fdfd7d0d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    22423.000000\n",
       "mean        84.805334\n",
       "std         13.248339\n",
       "min         35.000000\n",
       "25%         85.000000\n",
       "50%         90.000000\n",
       "75%         95.000000\n",
       "max        100.000000\n",
       "Name: safety_score, dtype: float64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women['safety_score'].describe()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f64a448-6c96-4f79-a605-22cf0cda2048",
   "metadata": {},
   "source": [
    "### 12. City-Wise Safety Ranking"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "18def190-876b-4678-8bfe-13ba5cf186ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "City\n",
       "Visakhapatnam    75.968137\n",
       "Agra             80.262582\n",
       "Ahmedabad        81.103582\n",
       "Varanasi         82.150000\n",
       "Bhopal           82.150538\n",
       "Bangalore        82.193928\n",
       "Indore           82.818182\n",
       "Vasai            82.889447\n",
       "Chennai          82.890152\n",
       "Hyderabad        83.419886\n",
       "Name: safety_score, dtype: float64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city_risk = (\n",
    "    df_women\n",
    "    .groupby('City')['safety_score']\n",
    "    .mean()\n",
    "    .sort_values()\n",
    ")\n",
    "\n",
    "city_risk.head(10)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63cc16d5-bd7d-4129-a1f7-3a455c2ab572",
   "metadata": {},
   "source": [
    "## 13. Save CLEAN & PROCESSED DATA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1941144d-b17c-4872-a51f-0306e498c111",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Processed data saved successfully.\n"
     ]
    }
   ],
   "source": [
    "os.makedirs('../data', exist_ok=True)\n",
    "\n",
    "df_women.to_csv(\n",
    "    '../data/processed_women_safety.csv',\n",
    "    index=False\n",
    ")\n",
    "\n",
    "print(\"Processed data saved successfully.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3ad26e22-27b6-4baa-8e02-ad14bfb3ca37",
   "metadata": {},
   "source": [
    "## 14. Save Trained Models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "62ffd214-020f-47c8-a340-5b9ce4ba7260",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Models saved successfully.\n"
     ]
    }
   ],
   "source": [
    "os.makedirs('../models', exist_ok=True)\n",
    "\n",
    "joblib.dump(kmeans, '../models/kmeans_model.pkl')\n",
    "joblib.dump(iso, '../models/isolation_forest.pkl')\n",
    "joblib.dump(scaler, '../models/scaler.pkl')\n",
    "joblib.dump(le_city, '../models/city_encoder.pkl')\n",
    "\n",
    "print(\"Models saved successfully.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de973186-c919-414d-af35-842cab226471",
   "metadata": {},
   "source": [
    "## Silhouette Score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "a40cf920-5497-4422-8b0f-42defa1d9862",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.15474939551309677"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import silhouette_score\n",
    "\n",
    "score = silhouette_score(X_scaled, df_women['cluster'])\n",
    "score\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
