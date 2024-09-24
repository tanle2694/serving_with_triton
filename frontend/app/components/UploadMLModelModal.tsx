import React, { useState } from 'react';
import styles from './UploadMLModelModal.module.css';

interface UploadMLModelModalProps {
    isOpen: boolean;
    onClose: () => void;
    onUpload: (modelData: any) => void;
}

const UploadMLModelModal: React.FC<UploadMLModelModalProps> = ({ isOpen, onClose, onUpload }) => {
    const [file, setFile] = useState<File | null>(null);
    const [name, setName] = useState('');
    const [type, setType] = useState('');
    const [description, setDescription] = useState('');

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        
        if (e.target.files) {
            setFile(e.target.files[0]);
        }
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (file && name) {
            const modelData = {
                file, name, type, description
            }
            onUpload(modelData);
            onClose();
        }
    };

    if (!isOpen) return null;

    return (
        <div className={styles.modalOverlay}>
        <div className={styles.modalContent}>
          <h2>Upload ML Model</h2>
          <form onSubmit={handleSubmit}>
            <div>
              <label htmlFor="file">Model File:</label>
              <input type="file" id="file" onChange={handleFileChange} required />
            </div>
            <div>
              <label htmlFor="name">Model Name:</label>
              <input type="text" id="name" value={name} onChange={(e) => setName(e.target.value)} required />
            </div>
            <div>
              <label htmlFor="type">Model Type:</label>
              <input type="text" id="type" value={type} onChange={(e) => setType(e.target.value)} />
            </div>
            <div>
              <label htmlFor="description">Description:</label>
              <textarea id="description" value={description} onChange={(e) => setDescription(e.target.value)} />
            </div>
            <div className={styles.modalActions}>
              <button type="submit">Upload</button>
              <button type="button" onClick={onClose}>Cancel</button>
            </div>
          </form>
        </div>
      </div>
    )
  };

  export default UploadMLModelModal;