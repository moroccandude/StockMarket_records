
#### Overview
This project provides a comprehensive weekly analysis of Bitcoin's evolution using a robust data pipeline built with Hadoop streaming, leveraging multiple technologies to fetch, process, and store cryptocurrency data.

###### Architecture
![architecture](https://github.com/user-attachments/assets/77f2a373-b953-41b4-a8db-2db2fd9a2b6a)

##### Data Flow
 **Data Source**: CoinGecko API
 **Ingestion**: Custom Python scripts
**Processing**: Hadoop MapReduce with Python
**Storage**: Apache HBase
**Visualization**: Streamlit (connected with LLM)

##### Components
- `fetcher.py`: Retrieves data from CoinGecko API
- `ingester.py`: Prepares and stages data for processing
- `Mapper.py`: Transforms and maps Bitcoin data
- `Reducer.py`: Aggregates and summarizes Bitcoin evolution metrics

##### 📦 Prerequisites
- Python 3.x
- docker
- Apache Hadoop
- Apache HBase
- CoinGecko API access

#### Getting Started

### Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   docker-compose up
   ```

### Configuration
1. Set up CoinGecko API credentials
2. Configure Hadoop and HBase connection parameters

### Running the Pipeline
```bash
# Fetch data
python fetcher.py

# Ingest data
python ingester.py

# Run Hadoop Streaming Job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input /path/to/input \
    -output /path/to/output \
    -mapper mapper.py \
    -reducer reducer.py
```

##### 🔍 Future Enhancements
- Real-time streaming support
- Advanced visualization
- Machine learning predictive models

##### 🤝 Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


###### 📧 Contact
Email : ismailsamilacc@gmail.com <br/>
Linkdin :  <a href="https://www.linkedin.com/in/ismail-samil-07753428a/">@ismailsamil</a>
