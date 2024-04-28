import { Linkedin } from "lucide-react";

import {
  Avatar,
  AvatarFallback,
  AvatarImage,
} from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card";


function ViLy() {
  return (
    <HoverCard>
      <HoverCardTrigger asChild>
        <a href="https://www.linkedin.com/in/vi-k-ly/" target="__blank">
        <Button className="p-0" variant="link">Vi K. Ly</Button>
        </a>
      </HoverCardTrigger>
      <HoverCardContent className="w-70">
        <div className="flex justify-between space-x-4">
          <Avatar>
            <AvatarImage src="https://media.licdn.com/dms/image/C4E03AQEOUmcDhOWTOA/profile-displayphoto-shrink_800_800/0/1638552696336?e=1718236800&v=beta&t=wWJCWyVk5iaryjsI3bdmIZgDnhXuc91NQC5MDdme4fU" />
            <AvatarFallback>VC</AvatarFallback>
          </Avatar>
          <div className="space-y-1">
            <h4 className="text-sm font-semibold">Vi K. Ly</h4>
            <p className="text-sm">
              Data Scientist.
            </p>
            <div className="flex items-center pt-2">
              <Linkedin className="mr-2 h-4 w-4 opacity-70" />{" "}
              <a href="https://www.linkedin.com/in/vi-k-ly/" target="__blank"><span className="text-xs text-muted-foreground">
                See LinkedIn
              </span>
              </a>
            </div>
          </div>
        </div>
      </HoverCardContent>
    </HoverCard>
  )
}

export default ViLy