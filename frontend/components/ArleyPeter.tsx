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

function ArleyPeter() {
  return (
    <HoverCard>
      <HoverCardTrigger asChild>
      <a href="https://www.linkedin.com/in/arley-peter/" target="__blank">
        <Button className="p-0" variant="link">Arley D. Peter</Button>
        </a>
      </HoverCardTrigger>
      <HoverCardContent className="w-70">
        <div className="flex justify-between space-x-4">
          <Avatar>
            <AvatarImage src="https://media.licdn.com/dms/image/D4D03AQGRBxVaEWA5dw/profile-displayphoto-shrink_400_400/0/1711559882025?e=1718236800&v=beta&t=_5-tEAIC5el9yeoDhB2YjkYzzRafbM-j47kxFO9qPXo" />
            <AvatarFallback>VC</AvatarFallback>
          </Avatar>
          <div className="space-y-1">
            <h4 className="text-sm font-semibold">Arley D. Peter</h4>
            <p className="text-sm">
              Full-Stack Software Engineer.
            </p>
            <div className="flex items-center pt-2">
              <Linkedin className="mr-2 h-4 w-4 opacity-70" />{" "}
              <a href="https://www.linkedin.com/in/arley-peter/" target="__blank">
              <span className="text-xs text-muted-foreground">
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

export default ArleyPeter