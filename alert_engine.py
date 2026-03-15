{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "31b95bdb-32bc-4634-8051-10803ca20b34",
   "metadata": {},
   "source": [
    "## Load Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "aac3eb98-b867-4068-bc3e-df9fc97d3e6b",
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
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>02-01-2020 00:00</td>\n",
       "      <td>01-01-2020 00:00</td>\n",
       "      <td>01-01-2020 01:11</td>\n",
       "      <td>Ahmedabad</td>\n",
       "      <td>576</td>\n",
       "      <td>IDENTITY THEFT</td>\n",
       "      <td>16</td>\n",
       "      <td>M</td>\n",
       "      <td>Blunt Object</td>\n",
       "      <td>Violent Crime</td>\n",
       "      <td>13</td>\n",
       "      <td>No</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>01-01-2020 19:00</td>\n",
       "      <td>01-01-2020 01:00</td>\n",
       "      <td>01-01-2020 06:26</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>128</td>\n",
       "      <td>HOMICIDE</td>\n",
       "      <td>37</td>\n",
       "      <td>M</td>\n",
       "      <td>Poison</td>\n",
       "      <td>Other Crime</td>\n",
       "      <td>9</td>\n",
       "      <td>No</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
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
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Report Number     Date Reported Date of Occurrence Time of Occurrence  \\\n",
       "0              1  02-01-2020 00:00   01-01-2020 00:00   01-01-2020 01:11   \n",
       "1              2  01-01-2020 19:00   01-01-2020 01:00   01-01-2020 06:26   \n",
       "2              3  02-01-2020 05:00   01-01-2020 02:00   01-01-2020 14:30   \n",
       "3              4  01-01-2020 05:00   01-01-2020 03:00   01-01-2020 14:46   \n",
       "4              5  01-01-2020 21:00   01-01-2020 04:00   01-01-2020 16:51   \n",
       "\n",
       "        City  Crime Code Crime Description  Victim Age Victim Gender  \\\n",
       "0  Ahmedabad         576    IDENTITY THEFT          16             M   \n",
       "1    Chennai         128          HOMICIDE          37             M   \n",
       "2   Ludhiana         271        KIDNAPPING          48             F   \n",
       "3       Pune         170          BURGLARY          49             F   \n",
       "4       Pune         421         VANDALISM          30             F   \n",
       "\n",
       "    Weapon Used   Crime Domain  Police Deployed Case Closed  Date Case Closed  \n",
       "0  Blunt Object  Violent Crime               13          No               NaN  \n",
       "1        Poison    Other Crime                9          No               NaN  \n",
       "2  Blunt Object    Other Crime               15          No               NaN  \n",
       "3       Firearm    Other Crime                1         Yes  29-04-2020 05:00  \n",
       "4         Other    Other Crime               18         Yes  08-01-2020 21:00  "
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(\"../Indian Crimes Dataset/crime_dataset_india.csv\")\n",
    "df.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a57fb805-77d8-49b2-bb4d-92a4e71a155c",
   "metadata": {},
   "source": [
    "## Number of rows and columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "00b4add5-3277-4260-985f-1702b3a61fb8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(40160, 14)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "605a8881-81b3-43e6-991d-230fd09d6d1b",
   "metadata": {},
   "source": [
    "## Column names This step decides: Which features we use , How we build safety score ,How we cluster"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "366b6b54-b3a2-44ed-9a75-b6afab9fc619",
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
    "\n",
    "df.columns\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0609e52c-8524-4252-9202-54f646ff112e",
   "metadata": {},
   "source": [
    "## Keep only Female victims"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3dad8192-7409-4c89-9139-db304ed5ffe8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(22423, 14)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women = df[df['Victim Gender'] == 'F'].copy()\n",
    "\n",
    "df_women.shape\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "83875e3f-eff3-4ab6-bb40-f42ab5b9dd43",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "os.makedirs('../data', exist_ok=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "1d7b9acd-dd53-4a05-9fde-bb72ec084abc",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_women.to_csv('../data/processed_women_safety.csv', index=False)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51224133-0ab2-4e32-ab15-2cc1c9e679c3",
   "metadata": {},
   "source": [
    "## Check crime types affecting women"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "99e9d608-b54c-4360-b43e-766362e5170a",
   "metadata": {},
   "source": [
    "## This tells us:\n",
    "\n",
    "### What types of crimes are common\n",
    "\n",
    "### Which crimes indicate unsafe areas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "953c93c6-2c2b-44a2-bdc5-23b6aae4069d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_women['Date of Occurrence'] = pd.to_datetime(\n",
    "    df_women['Date of Occurrence'],\n",
    "    errors='coerce'\n",
    ")\n",
    "\n",
    "df_women['Date Reported'] = pd.to_datetime(\n",
    "    df_women['Date Reported'],\n",
    "    errors='coerce'\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "096d3658-1ae5-40d4-9f42-ce11ca8f4d32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date of Occurrence        0\n",
       "Date Reported         13503\n",
       "dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women[['Date of Occurrence', 'Date Reported']].isna().sum()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1f5725ae-6a56-490d-9b71-023fc9b2687a",
   "metadata": {},
   "source": [
    "## Convert Date & Time (Feature Engineering)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d5a5b2ab-0d50-49c1-8134-722f01351de8",
   "metadata": {},
   "source": [
    "### Convert dates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "97d2bc43-9cea-4d24-bcad-aa6130a22a93",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_women['hour'] = pd.to_datetime(\n",
    "    df_women['Time of Occurrence'],\n",
    "    errors='coerce',\n",
    "    format='%H:%M'\n",
    ").dt.hour\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8d542f87-0b0a-4570-9ac4-c66ae7aedf6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\user\\anaconda3\\envs\\women_safety_env\\lib\\site-packages\\numpy\\lib\\_nanfunctions_impl.py:1215: RuntimeWarning: Mean of empty slice\n",
      "  return np.nanmean(a, axis, out=out, keepdims=keepdims)\n"
     ]
    }
   ],
   "source": [
    "df_women['hour'] = df_women['hour'].fillna(df_women['hour'].median())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "690501e4-d735-4dbd-a53b-439bbb86e2ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2     01-01-2020 14:30\n",
       "3     01-01-2020 14:46\n",
       "4     01-01-2020 16:51\n",
       "6     01-01-2020 14:08\n",
       "12    01-01-2020 23:14\n",
       "14    01-01-2020 22:28\n",
       "15    01-01-2020 18:54\n",
       "17    01-01-2020 23:09\n",
       "19    02-01-2020 18:02\n",
       "20    02-01-2020 02:33\n",
       "Name: Time of Occurrence, dtype: object"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women['Time of Occurrence'].head(10)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "dc41eaf5-c7cd-4739-a083-8f077d74979a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_women['hour'] = pd.to_datetime(\n",
    "    df_women['Time of Occurrence'],\n",
    "    errors='coerce'\n",
    ").dt.hour\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1ffcafde-3559-4c03-9033-96dc0cb8dca7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    8919.000000\n",
       "mean       11.401727\n",
       "std         6.885111\n",
       "min         0.000000\n",
       "25%         5.000000\n",
       "50%        11.000000\n",
       "75%        17.000000\n",
       "max        23.000000\n",
       "Name: hour, dtype: float64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women['hour'].isna().sum()\n",
    "df_women['hour'].describe()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "6eb35588-2da5-4b35-ad82-74ce3e250e6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_women['hour'] = df_women['hour'].fillna(df_women['hour'].median())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "cfa98e5a-f282-426e-a0ad-94b306d32e61",
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
       "      <th>Date of Occurrence</th>\n",
       "      <th>Time of Occurrence</th>\n",
       "      <th>hour</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2020-01-01 02:00:00</td>\n",
       "      <td>01-01-2020 14:30</td>\n",
       "      <td>14.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2020-01-01 03:00:00</td>\n",
       "      <td>01-01-2020 14:46</td>\n",
       "      <td>14.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2020-01-01 04:00:00</td>\n",
       "      <td>01-01-2020 16:51</td>\n",
       "      <td>16.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2020-01-01 06:00:00</td>\n",
       "      <td>01-01-2020 14:08</td>\n",
       "      <td>14.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>2020-01-01 12:00:00</td>\n",
       "      <td>01-01-2020 23:14</td>\n",
       "      <td>23.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Date of Occurrence Time of Occurrence  hour\n",
       "2  2020-01-01 02:00:00   01-01-2020 14:30  14.0\n",
       "3  2020-01-01 03:00:00   01-01-2020 14:46  14.0\n",
       "4  2020-01-01 04:00:00   01-01-2020 16:51  16.0\n",
       "6  2020-01-01 06:00:00   01-01-2020 14:08  14.0\n",
       "12 2020-01-01 12:00:00   01-01-2020 23:14  23.0"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women[['Date of Occurrence', 'Time of Occurrence', 'hour']].head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "31962c80-7fba-469c-9a76-dc8d39697921",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_women['month'] = df_women['Date of Occurrence'].dt.month\n",
    "df_women['dayofweek'] = df_women['Date of Occurrence'].dt.dayofweek\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "58f5f20b-ecc7-4f75-9f7c-b8900f2cf265",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "le_city = LabelEncoder()\n",
    "df_women['city_encoded'] = le_city.fit_transform(df_women['City'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "06824d11-831e-4644-938d-70beecdd817b",
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
       "      <th>city_encoded</th>\n",
       "      <th>hour</th>\n",
       "      <th>Victim Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>15</td>\n",
       "      <td>14.0</td>\n",
       "      <td>48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>21</td>\n",
       "      <td>14.0</td>\n",
       "      <td>49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>21</td>\n",
       "      <td>16.0</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>4</td>\n",
       "      <td>14.0</td>\n",
       "      <td>64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>28</td>\n",
       "      <td>23.0</td>\n",
       "      <td>36</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    city_encoded  hour  Victim Age\n",
       "2             15  14.0          48\n",
       "3             21  14.0          49\n",
       "4             21  16.0          30\n",
       "6              4  14.0          64\n",
       "12            28  23.0          36"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = df_women[['city_encoded', 'hour', 'Victim Age']]\n",
    "X.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "8ffe76a5-ce69-4547-9601-92f49c610701",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "scaler = StandardScaler()\n",
    "X_scaled = scaler.fit_transform(X)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f275acef-82cf-45e8-b7d0-d665e33008e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.cluster import KMeans\n",
    "\n",
    "kmeans = KMeans(n_clusters=4, random_state=42)\n",
    "df_women['cluster'] = kmeans.fit_predict(X_scaled)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5edd2752-4302-4481-b126-3ffc35f1d26e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cluster\n",
       "2    6813\n",
       "3    6645\n",
       "1    6368\n",
       "0    2597\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women['cluster'].value_counts()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "4fa92758-4b93-43bb-907c-2f9d8ea70fd1",
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
       "      <td>3.051598</td>\n",
       "      <td>44.420870</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>12.190484</td>\n",
       "      <td>26.349089</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>12.209159</td>\n",
       "      <td>41.801556</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>12.265011</td>\n",
       "      <td>63.910609</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              hour  Victim Age\n",
       "cluster                       \n",
       "0         3.051598   44.420870\n",
       "1        12.190484   26.349089\n",
       "2        12.209159   41.801556\n",
       "3        12.265011   63.910609"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women.groupby('cluster')[['hour', 'Victim Age']].mean()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "f3ff7742-371e-4a5e-93ff-27ed9a4b902a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cluster  City     \n",
       "0        Delhi        322\n",
       "         Mumbai       286\n",
       "         Bangalore    218\n",
       "         Hyderabad    189\n",
       "         Kolkata      184\n",
       "         Chennai      163\n",
       "         Pune         131\n",
       "         Lucknow      122\n",
       "         Ahmedabad    113\n",
       "         Jaipur       109\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women.groupby('cluster')['City'].value_counts().head(10)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "e47cd6ba-936a-4024-ae7c-8961bceb6b5b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import IsolationForest\n",
    "\n",
    "iso = IsolationForest(\n",
    "    contamination=0.1,   # 10% unusual incidents\n",
    "    random_state=42\n",
    ")\n",
    "\n",
    "df_women['anomaly'] = iso.fit_predict(X_scaled)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7c8226c9-cedd-4526-89ec-328220fd7f07",
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
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women['anomaly'].value_counts()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "55b488e1-6887-4690-9b20-e2d338a24789",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "anomaly\n",
       "-1    11.090504\n",
       " 1    11.167493\n",
       "Name: hour, dtype: float64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women.groupby('anomaly')['hour'].mean()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "606ab0fc-bc81-4eba-9abb-0ca9634ab650",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_women['unsafe_cluster'] = (df_women['cluster'] == 0).astype(int)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "09444786-6891-474c-b234-174ea9f16909",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_women['safety_score'] = (\n",
    "    100\n",
    "    - df_women['unsafe_cluster'] * 30\n",
    "    - (df_women['anomaly'] == -1) * 30\n",
    "    - (df_women['hour'] >= 20) * 20\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "9e5bb105-da6e-4ab5-89ab-0f781d414af5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    22423.000000\n",
       "mean        92.251706\n",
       "std         16.827356\n",
       "min         40.000000\n",
       "25%        100.000000\n",
       "50%        100.000000\n",
       "75%        100.000000\n",
       "max        100.000000\n",
       "Name: safety_score, dtype: float64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women['safety_score'].describe()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "63b7b451-55bc-4c86-a724-8cf4b97d3fd9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    22423.000000\n",
       "mean        92.251706\n",
       "std         16.827356\n",
       "min         40.000000\n",
       "25%        100.000000\n",
       "50%        100.000000\n",
       "75%        100.000000\n",
       "max        100.000000\n",
       "Name: safety_score, dtype: float64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_women['safety_score'].describe()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "3e37c306-6e05-43f2-a2f2-a25d255131cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "City\n",
       "Visakhapatnam    81.789216\n",
       "Varanasi         87.250000\n",
       "Vasai            87.889447\n",
       "Agra             88.336980\n",
       "Thane            88.421053\n",
       "Srinagar         89.794872\n",
       "Ahmedabad        90.358180\n",
       "Surat            90.760870\n",
       "Patna            91.189873\n",
       "Nashik           91.319797\n",
       "Name: safety_score, dtype: float64"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city_risk = df_women.groupby('City')['safety_score'].mean().sort_values()\n",
    "city_risk.head(10)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "f8ab0c60-fd91-4749-b869-8d709ce4e180",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "os.makedirs('../models', exist_ok=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "8a64eee6-6020-44c9-a643-0e5780836c4e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['../models/city_encoder.pkl']"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import joblib\n",
    "\n",
    "joblib.dump(kmeans, '../models/kmeans_model.pkl')\n",
    "joblib.dump(iso, '../models/isolation_forest.pkl')\n",
    "joblib.dump(scaler, '../models/scaler.pkl')\n",
    "joblib.dump(le_city, '../models/city_encoder.pkl')\n"
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
