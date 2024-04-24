"use client"
import UploadForm from "@/components/UploadForm";
import ArleyPeter from "@/components/ArleyPeter";
import BloodChart from "@/components/BloodChart";
import ViLy from "@/components/ViLy";
import { Progress } from "@/components/ui/progress";
import { useState, useEffect } from "react";
import Image from "next/image";

import hemocount_logo from "@/public/hemocount-logo.png";

export default function Home() {
  const [buttonClicked, setButtonClicked] = useState(false);
  const [progressValue, setProgressValue] = useState(0);
  const [uploadComplete, setUploadComplete] = useState(false);
  const [bloodData, setBloodData] = useState<any>(null);

  const handleButtonClick = () => {
    setButtonClicked(true);
    console.log('Button clicked in UploadForm!');
  };

  const handleUploadComplete = (data: any) => {
    console.log('Upload complete:', data);
    setUploadComplete(true);
    setBloodData(data);
  };

  useEffect(() => {
    let interval: NodeJS.Timeout;

    const uploadProgress = () => {
      if (!uploadComplete && progressValue < 95) {
        setProgressValue(prevValue => prevValue + 1);
      } else if (uploadComplete && progressValue < 100) {
        setProgressValue(prevValue => prevValue + 5);
      } else {
        clearInterval(interval);
      }
    };

    interval = setInterval(uploadProgress, 100);

    return () => {
      clearInterval(interval);
    };
  }, [uploadComplete, progressValue]);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <Image src={hemocount_logo} alt="HemoCountAI Logo" />
      {/* <h1 className="text-4xl font-bold">HemoCountAI</h1> */}
      {buttonClicked ? (
        uploadComplete ? (
          <BloodChart bloodData={bloodData} />
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
