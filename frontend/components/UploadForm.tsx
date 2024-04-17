import { useState } from 'react';

interface UploadFormProps {
    onButtonClick: () => void;
    onUploadComplete: (data: any) => void; // Add this line
  }

function UploadForm({ onButtonClick, onUploadComplete }: UploadFormProps) {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [buttonClicked, setButtonClicked] = useState(false);

const handleButtonClick = () => {
setButtonClicked(true);
onButtonClick();
};

const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0] || null;
    setSelectedFile(file);
};

  const handleSubmit = async () => {
    if (selectedFile) {
      try {
        handleButtonClick();
        const formData = new FormData();
        formData.append('file', selectedFile);

        const response = await fetch('http://localhost:5000/get_blood_cells', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          const responseData = await response.json();
          console.log('File uploaded successfully!');
          console.log(responseData);
          onUploadComplete(responseData); // Add this line
        } else {
          console.error('Error uploading file:', response.statusText);
        }
      } catch (error) {
        console.error('An error occurred:', error);
      }
    } else {
      console.warn('No file selected.');
    }
  };

  return (
    <div>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      <button onClick={handleSubmit}>Upload</button>
    </div>
  );
}

export default UploadForm;
