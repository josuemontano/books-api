import React, { useCallback, useEffect, useState } from "react";
import { GetPiDocument } from "../generated/graphql";
import { createWebSocketClient } from "./lib";

export default function PiSeries() {
  const [value, setValue] = useState(0);
  const subscribe = useCallback(async () => {
    const wsClient = await createWebSocketClient("ws://localhost:8000/graphql");
    await new Promise<void>(() => {
      wsClient.subscribe(
        GetPiDocument,
        {
          next: (data) => {
            setValue(data.pi);
          },
        },
        { precision: 10 }
      );
    });
  }, []);

  useEffect(() => {
    subscribe();
  }, []);

  return <p>Pi: {value}</p>;
}
