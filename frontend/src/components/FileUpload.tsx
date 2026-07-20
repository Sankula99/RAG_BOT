import React, { useState, ChangeEvent } from 'react';

const FileUpload: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [status, setStatus] = useState<string>('Idle');

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    setUploading(true);
    setStatus('Uploading...');
    try {
      const formData = new FormData();
      formData.append('file', file);
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) {
        throw new Error('Upload failed');
      }
      setStatus('Upload successful!');
    } catch (error) {
      console.error('Error uploading file:', error);
      setStatus('Upload failed.');
    } finally {
      setUploading(false);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Upload a File</h2>
      <input type="file" onChange={handleFileChange} disabled={uploading} />
      <button onClick={handleUpload} disabled={!file || uploading} style={{ marginLeft: '10px' }}>
        {uploading ? 'Uploading...' : 'Upload'}
      </button>
      <p>Status: {status}</p>
    </div>
  );
};

export default FileUpload;