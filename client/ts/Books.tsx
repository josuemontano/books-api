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
    <div className="p-4 sm:p-6 lg:p-8">
      <div className="sm:flex sm:items-center">
        <div className="sm:flex-auto">
          <h1 className="text-2xl font-semibold text-gray-900 dark:text-slate-200 uppercase">
            Books
          </h1>
          <p className="mt-2 text-sm text-gray-700 dark:text-slate-300">
            A list of all the books including their title, author, and
            publisher.
          </p>
        </div>
        <div className="mt-4 sm:mt-0 sm:ml-16 sm:flex-none"></div>
      </div>
      <div className="mt-8 flex flex-col">
        <div className="-my-2 -mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div className="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
            <div className="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg">
              <table className="min-w-full divide-y divide-gray-300 dark:divide-slate-500">
                <thead className="bg-gray-50 dark:bg-slate-800">
                  <tr>
                    <th
                      scope="col"
                      className="py-3 pl-4 pr-3 text-left text-xs font-medium uppercase tracking-wide text-gray-500 dark:text-slate-200 sm:pl-6"
                    >
                      Title
                    </th>
                    <th
                      scope="col"
                      className="px-3 py-3 text-left text-xs font-medium uppercase tracking-wide text-gray-500 dark:text-slate-200"
                    >
                      Description
                    </th>
                    <th
                      scope="col"
                      className="px-3 py-3 text-left text-xs font-medium uppercase tracking-wide text-gray-500 dark:text-slate-200"
                    >
                      Author
                    </th>
                    <th
                      scope="col"
                      className="px-3 py-3 text-left text-xs font-medium uppercase tracking-wide text-gray-500 dark:text-slate-200"
                    >
                      Publisher
                    </th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-200 bg-white dark:bg-slate-800 dark:divide-gray-700">
                  {data.books.edges.map((edge) => (
                    <tr key={edge.cursor}>
                      <td className="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 dark:text-slate-500 sm:pl-6">
                        {edge.node.title}
                      </td>
                      <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500 dark:text-slate-500">
                        {edge.node.description}
                      </td>
                      <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500 dark:text-slate-500">
                        {edge.node.author.name}
                      </td>
                      <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500 dark:text-slate-500">
                        {edge.node.publisher.name}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
