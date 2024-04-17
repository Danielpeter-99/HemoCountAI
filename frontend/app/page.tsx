"use client"
import UploadForm from "@/components/UploadForm";
import ArleyPeter from "@/components/ArleyPeter";
import BloodChart from "@/components/BloodChart";
import ViLy from "@/components/ViLy";
import { Progress } from "@/components/ui/progress";
import { useState, useEffect } from "react";

export default function Home() {
  const [buttonClicked, setButtonClicked] = useState(false);
  const [progressValue, setProgressValue] = useState(0);
  const [uploadComplete, setUploadComplete] = useState(false);
  const [bloodData, setBloodData] = useState<any>(null); // State to store the blood data

  const handleButtonClick = () => {
    setButtonClicked(true);
    console.log('Button clicked in UploadForm!');
  };

  const handleUploadComplete = (data: any) => {
    console.log('Upload complete:', data);
    setUploadComplete(true);
    setBloodData(data); // Set the blood data once upload is complete
  };

  useEffect(() => {
    let interval: NodeJS.Timeout;

    const uploadProgress = () => {
      if (!uploadComplete && progressValue < 95) {
        setProgressValue(prevValue => prevValue + 1);
      } else if (uploadComplete && progressValue < 100) {
        setProgressValue(prevValue => prevValue + 5); // Jump faster towards 100%
      } else {
        clearInterval(interval);
      }
    };

    interval = setInterval(uploadProgress, 100); // Adjust the interval timing

    return () => {
      clearInterval(interval);
    };
  }, [uploadComplete, progressValue]);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">HemoCountAI</h1>
      {buttonClicked ? (
        uploadComplete ? (
          <BloodChart bloodData={bloodData} /> // Pass bloodData to BloodChart when upload is complete
        ) : (
          <Progress value={progressValue} />
        )
      ) : (
        <UploadForm onButtonClick={handleButtonClick} onUploadComplete={handleUploadComplete} />
      )}
      <p className="font-light">By <ViLy/> and <ArleyPeter/>.</p>
    </main>
  );
}
