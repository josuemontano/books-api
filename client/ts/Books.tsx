import React, { useEffect, useState } from "react";
import { GetAllBooksQuery } from "../generated/graphql";
import { sdk } from "./lib";

export default function Books() {
  const [data, setData] = useState<GetAllBooksQuery | undefined>(undefined);

  useEffect(() => {
    sdk.getAllBooks({ first: 10 }).then(setData);
  }, []);

  if (data === undefined) return <p>Loading</p>;
  return (
    <div>
      <h1>You have {data.books.totalCount} books</h1>
      <ul>
        {data.books.edges.map((edge) => (
          <p key={edge.cursor}>{edge.node.title}</p>
        ))}
      </ul>
    </div>
  );
}
