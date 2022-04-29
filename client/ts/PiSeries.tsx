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

  return (
    <div>
      <div>
        <dl className="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-3">
          <div />
          <div className="px-4 py-5 bg-white dark:bg-slate-800 shadow rounded-lg overflow-hidden sm:p-6">
            <dt className="text-sm font-medium text-gray-500 truncate">
              Leibniz's series Pi
            </dt>
            <dd className="mt-1 text-3xl font-semibold text-gray-900 dark:text-slate-300">
              {value}
            </dd>
          </div>
          <div />
        </dl>
      </div>
    </div>
  );
}
