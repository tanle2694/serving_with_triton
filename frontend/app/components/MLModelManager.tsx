import React, { useState, useEffect } from 'react';
import styles from './MLModelManager.module.css';

interface MLModel {
  id: string;
  name: string;
  type: string;
  description: string;
  createdAt: string;
  lastActive: string;
  status: 'active' | 'inactive';
}

const MLModelManager: React.FC = () => {
  const [models, setModels] = useState<MLModel[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const BACKEND_SERVER_HOST = '0.0.0.0';
  const BACKEND_SERVER_PORT = '8000'
  
  useEffect(() => {
    // Fetch models from API
    const fetchModels = async () => {
        setIsLoading(true);
        try {
            
            const response = await fetch(`http://${BACKEND_SERVER_HOST}:${BACKEND_SERVER_PORT}/api/models`);
            if (!response.ok) {
                throw new Error('Failed to fetch models');
            }
            const data: MLModel[] = await response.json();
            console.log("data", data);
            setModels(data);
            setError(null);
        } catch (error) {
            setError('Error fetching models. Please try again later.');
            console.error('Error fetching models:', error);
        } finally {
            setIsLoading(false);
        }
    };

    fetchModels();
  }, []);

  return (
    <div className={styles.container}>
      <div className={styles.actions}>
        <button className={styles.actionButton}>Upload ML Model</button>
        <button className={styles.actionButton}>Refresh</button>
        <button className={styles.actionButton}>Filter</button>
        <button className={styles.actionButton}>Delete</button>
        
      </div>
      <div className={styles.searchContainer}>
        <input type="text" placeholder="Search" className={styles.searchInput} />
      </div>
      {isLoading ? (
        <p>Loading models...</p>
      ) : error ? (
        <p className={styles.error}>{error}</p>
      ) : (                          
        <table className={styles.modelTable}>
            <thead>
            <tr>
                <th></th>
                <th>Model Name</th>
                <th>Model Type</th>            
                <th>Description</th>
                <th>Last Active</th>
                <th>Created At</th>
                <th>Status</th>
                <th>Action</th>
            </tr>
            </thead>
            <tbody>
            {models.map((model) => (
                <tr key={model.id}>
                <td><input type="checkbox" /></td>
                <td>{model.name}</td>
                <td>{model.type}</td>              
                <td>{model.description}</td>
                <td>{model.lastActive}</td>
                <td>{model.createdAt}</td>
                <td>
                    <span className={`${styles.status} ${styles[model.status]}`}>
                    {model.status === 'active' ? '●' : '○'}
                    </span>
                </td>
                <td>
                    <button className={styles.actionButton}>●●●</button>
                </td>
                </tr>
            ))}
            </tbody>
        </table>
        
        
      )
      }
    </div>
  );
};

export default MLModelManager;